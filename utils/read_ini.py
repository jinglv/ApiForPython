from configparser import ConfigParser


class ReadIni(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_init()

    def read_init(self):
        read_ini = ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    # 通过key获取对应的value
    def get_value(self, section, key):
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value

if __name__ == '__main__':
    file_path = "/Users/lvjing/PycharmProjects/AppiumForPython/config/local_element.ini"
    read_ini = ReadIni(file_path)
    print(read_ini.get_value("login_element", "username"))
    print(read_ini.get_value("xxx", "xxx"))
