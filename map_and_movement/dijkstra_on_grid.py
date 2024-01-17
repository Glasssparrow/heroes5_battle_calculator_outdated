

class SquareMatrix:
    def __init__(self, size, value,
                 diagonal_value: int = "same_as_value_#987165451"):
        if diagonal_value == "same_as_value_#987165451":
            diagonal_value = value
        self.matrix = [value] * size**2
        self.size = size
        for x in range(size):
            self.matrix[x+x*size] = diagonal_value

    def _is_coord(self, value):
        if not isinstance(value, (list, tuple)):
            raise Exception(
                "Индекс не кортеж и не словарь"
            )
        elif len(value) != 2:
            raise Exception(
                "Количество координат не 2"
            )
        if value[0] >= self.size:
            raise Exception(
                f"Координата х ({value[0]}) "
                f"больше размерности матрицы ({self.size}). "
                f"Помните что нумерация начинается с 0."
            )
        elif value[1] >= self.size:
            raise Exception(
                f"Координата у ({value[1]}) "
                f"больше размерности матрицы ({self.size}). "
                f"Помните что нумерация начинается с 0."
            )

    @staticmethod
    def _is_number(value):
        if not isinstance(value, (int, float)):
            raise Exception(
                f"{value} не число (не экземпляр класса float или int)"
            )

    def get_row(self, row_number):
        start_point = row_number*self.size
        end_point = (row_number+1)*self.size
        return self.matrix[start_point:end_point]

    def __getitem__(self, item):
        self._is_coord(item)
        return self.matrix[item[0] + item[1] * self.size]

    def __setitem__(self, key, value):
        self._is_coord(key)
        self._is_number(value)
        self.matrix[key[0] + key[1]*self.size] = value

    def __delitem__(self, key):
        self._is_coord(key)
        self.matrix[key[0] + key[1]*self.size] = 0


class Path:
    def __init__(self, x, y, length):
        """Под длиной понимается ширина карты. x, y координаты старта"""
        self.range = {}
        self.path = {}
        self.len_x = length
        self.start_node = self._coord_into_node_number(x, y)
        self.for_iterator = []
        self.iteration = 0

    def _coord_into_node_number(self, x, y):
        return x + y * self.len_x

    def _node_number_into_coord(self, number):
        return number % self.len_x, number // self.len_x

    def __getitem__(self, item):
        return self.range[
            self._coord_into_node_number(item[0], item[1])
        ]

    def _get_path(self, node_number):
        if node_number not in self.path:
            raise Exception(
                "Невозможно достичь узла."
            )
        current_node = node_number
        path = []
        while current_node != self.start_node:
            path.append(self.path[current_node])
            current_node = self.path[current_node]
        result = []
        for x in path:
            result.append(self._node_number_into_coord(x))
        return result

    def get_path(self, x, y):
        result = self._get_path(
            self._coord_into_node_number(x, y)
        )
        return result

    def __setitem__(self, key, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2
        ):
            raise Exception(
                f"Передаваемые данные (сейчас - {value}) "
                f"должны быть в формате (number, number,)"
            )
        self.range[
            self._coord_into_node_number(key[0], key[1])
        ] = value[0]
        self.path[
            self._coord_into_node_number(key[0], key[1])
        ] = value[1]

    def __delitem__(self, key):
        del self.range[
            self._coord_into_node_number(key[0], key[1])
        ]
        del self.path[
            self._coord_into_node_number(key[0], key[1])
        ]

    def __iter__(self):
        for k in self.range.keys():
            self.for_iterator.append(k)
        self.for_iterator.sort()
        self.iteration = -1
        return self

    def __next__(self):
        """Возвращает (х, у), длина_пути, [координаты, пути]"""
        self.iteration += 1
        if self.iteration < len(self.for_iterator):
            node_number = self.for_iterator[self.iteration]
            return (
                self._node_number_into_coord(node_number),
                self.range[node_number],
                self._get_path(node_number),
            )
        else:
            raise StopIteration

    def __contains__(self, item):
        """Проверяет, входит ли ячейка с данными координатами в диапазон"""
        if not isinstance(item, tuple) or len(item) != 2:
            raise Exception(
                "Проверяется только входят ли координаты в диапазон. "
                "Координат должно быть две и они должны быть "
                "предоставлены в виде кортежа (х, у,)."
            )
        node_number = self._coord_into_node_number(item[0], item[1])
        if node_number in self.range.keys():
            return True
        else:
            return False


class Pathfinder:
    def __init__(self, height, length):
        self.all_nodes = []
        self.map_length = length
        self.map_height = height
        for y in range(height):
            for x in range(length):
                self.all_nodes.append(x + y * length)
        self.matrix = SquareMatrix(
            size=len(self.all_nodes), value=float("inf"),
            diagonal_value=0,
        )
        for y in self.all_nodes:
            for x in self.all_nodes:
                if abs(x-y) == 1 or abs(x-y) == self.map_length:
                    self.matrix[x, y] = 1
        self.occupied_cells = []

    def occupy_cell(self, x, y):
        if (x, y) not in self.occupied_cells:
            self.occupied_cells.append((x, y,))

    def empty_cell(self, x, y):
        element_number = -1
        for i, cell in enumerate(self.occupied_cells):
            if cell[0] == x and cell[1] == y:
                element_number = i
                break
        if element_number != -1:
            self.occupied_cells.pop(element_number)
        else:
            raise Exception(
                f"{x, y} не найдено в списке занятых союзниками "
                f"ячеек."
            )

    def _node_number_into_coord(self, number):
        return number % self.map_length, number // self.map_length

    def _coord_into_node_number(self, x, y):
        return x + y * self.map_length

    def _verify_cell(self, x, y):
        if x >= self.map_length:
            raise Exception(
                f"х ({x}) больше размерности поля ({self.map_length}). "
                f"Помните что нумерация с 0."
            )
        elif y >= self.map_height:
            raise Exception(
                f"y ({y}) больше размерности поля ({self.map_height}). "
                f"Помните что нумерация с 0."
            )

    def _block_cell_on_map(self, matrix, x, y, reverse):
        if reverse:
            value = 1
        else:
            value = float("inf")
        self._verify_cell(x, y)
        for dx in [-1, 1]:
            if (
                0
                <= (self._coord_into_node_number(x, y)+dx) <
                len(self.all_nodes)
            ):
                matrix[
                    self._coord_into_node_number(x, y)+dx,
                    self._coord_into_node_number(x, y)
                ] = value
        for dy in [-self.map_length, +self.map_length]:
            if (
                    0
                    <= (self._coord_into_node_number(x, y) + dy) <
                    len(self.all_nodes)
            ):
                matrix[
                    self._coord_into_node_number(x, y),
                    self._coord_into_node_number(x, y)+dy
                ] = value

    def _get_nodes_around(self, x, y, distance):
        nodes = []
        for node in self.all_nodes:
            node_x, node_y = self._node_number_into_coord(node)
            if (
                abs(node_x - x) + abs(node_y - y) <= distance and
                node != self._coord_into_node_number(x, y)
            ):
                nodes.append(node)
        return nodes

    def block_cell(self, x, y, reverse=False):
        self._block_cell_on_map(self.matrix, x, y, reverse)

    def unblock_cell(self, x, y):
        self.block_cell(x, y, reverse=True)

    def __call__(self, x, y, distance):
        paths = Path(x, y, self.map_length)
        paths[x, y] = (
            0,
            self._coord_into_node_number(x, y)
        )
        nodes = self._get_nodes_around(x, y, distance)
        start_node = self._coord_into_node_number(x, y)
        done_nodes = {start_node}
        best_path = {}
        last_row = [float("inf")] * self.matrix.size
        last_row[start_node] = 0

        while start_node != -1:
            current_row = self.matrix.get_row(start_node)
            for current_node in nodes:
                if current_node in done_nodes:
                    continue
                length = (
                        current_row[current_node] +
                        last_row[start_node]
                )
                if length < last_row[current_node]:
                    best_path[current_node] = start_node
                    last_row[current_node] = length

            min_len_node = -1
            max_len = float("inf")
            for current_node in nodes:
                if current_node in done_nodes:
                    continue
                if last_row[current_node] < max_len:
                    max_len = last_row[current_node]
                    min_len_node = current_node
            start_node = min_len_node
            if start_node != -1:
                done_nodes.add(start_node)

        for node in nodes:
            x, y = self._node_number_into_coord(node)
            if not (x, y) in self.occupied_cells:
                paths[x, y] = last_row[node], best_path[node]
        return paths
