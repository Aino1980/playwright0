import time


class As_dict:
    def as_dict(self):
        # return_dict = self.__dict__
        # temp_dict = self.__dict__.copy()
        # for key, value in temp_dict.items():
        #     if value == "":
        #         return_dict.pop(key)
        #         continue
        #     if "时间戳" in value:
        #         value = str(value).replace("时间戳", str(time.time_ns()))
        #         return_dict.update({key: value})
        # return return_dict
        return_dict = self.__dict__
        temp_dict = self.__dict__.copy()
        for key, value in temp_dict.items():
            if "时间戳" in value:
                value = str(value).replace("时间戳", str(time.time_ns()))
                return_dict.update({key: value})
        return return_dict