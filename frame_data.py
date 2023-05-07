class FrameData:
    """
    =========================================
                Global Variables
    =========================================
    """
    _frame_number = 0
    _uniq_objects_counter = 0
    _data = []

    """
    =========================================
                Global Methods
    =========================================
    """
    def __init__(self, frame_number, count, data):
        self.frame_number = frame_number
        self._uniq_objects_counter = count
        self._data = data

    def set_frame_number(self, frame_number):
        self._frame_number = frame_number

    def set_uniq_objects_counter(self, count):
        self._uniq_objects_counter = count

    def set_data(self, data):
        self._data = data

    def get_frame_number(self):
        return self._frame_number

    def get_uniq_objects_counter(self):
        return self._uniq_objects_counter

    def get_data(self):
        return self._data
