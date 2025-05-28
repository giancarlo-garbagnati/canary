import utils.io_utils as utils

def main():
    print('test')
    d = {
        'test':'test',
        'data':[1,2,3]
    }
    uri = ''
    utils.write_yaml(d, uri)

if __name__ == "__main__":
    main()