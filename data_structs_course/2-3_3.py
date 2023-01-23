class Table:
    
    def __init__(self, size) -> None:
        self.size = size
        self.link = None

    @staticmethod
    def merge(destination, source) -> int:
        # finding real tables
        while destination.link != None:
            destination = destination.link

        path_from_sourse = [source]

        while source.link != None:
            source = source.link
            path_from_sourse.append(source)

        if destination != source:
            destination.size += source.size
            source.size = 0
            for table in path_from_sourse: table.link = destination

            return destination.size

        return -1


def main():
    n, m = map(int, input().split())
    tables = list(map(Table, map(int, input().split())))

    max_size = max(tables, key=lambda t: t.size).size

    for i in range(m):
        destination, source = map(int, input().split())
        size = Table.merge(tables[destination-1], tables[source-1])
        if size > max_size: max_size = size

        print(max_size)

    
if __name__ == '__main__': main()