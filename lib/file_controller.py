

class FileController(object):
     def __init__(self):
         return

     def load_mots_file(self):
         f = open('uniq_mots_id.txt', 'r')
         x = f.read().splitlines()
         f.close()
         return x
