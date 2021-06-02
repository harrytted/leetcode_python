# coding: utf-8
class CopyFile:
    def __init__(self):
        self.db_data = [
            {'id': 1, 'name': 'root', 'parent_id': None},
            {'id': 2, 'name': 'two', 'parent_id': 1},
            {'id': 3, 'name': 'three', 'parent_id': 2},
            {'id': 4, 'name': 'four', 'parent_id': 2},
        ]
        self.max_id = max([x['id'] for x in self.db_data])

    def load_all(self):
        return self.db_data

    def save(self, name, parent_id):
        self.max_id += 1
        self.db_data.append({
            'id': self.max_id, 'name': name, 'parent_id': parent_id
        })
        return self.max_id

    def copy_file(self, file_id, parent_id):
        length = len(self.db_data)
        enumerate
        file_id = int(file_id)
        if file_id > length or not parent_id:
            return
        need_save_data = self.db_data[file_id-1:]
        for idx, data in enumerate(need_save_data):
            if idx == 0:
                # 特殊处理第一条数据
                if data.get('id') != int(file_id) or data.get('parent_id') != int(parent_id):
                    # 当给出的file_id, parent_id在存在的数据中找不到时，退出，说明给的数据不存在数据库中
                    return
            else:
                parent_id = length + 1
            self.save(data.get('name'), parent_id)


if __name__ == '__main__':
    copy_file = CopyFile()
    copy_file.copy_file(2, 1)
    print(copy_file.load_all())
