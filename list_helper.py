"""
    定义项目中所有对容器的操作。
"""

class ListHelper:
    """
        列表助手类
    """
    @staticmethod
    def find_all(iterable_target,func_condition):
        """
            在可迭代对象中，查找满足条件的所有元素。
        :param iterable_target:可迭代对象
        :param func_condition:所有条件
        :return:生成器对象
        """
        for item in iterable_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_one(iterable_target, func_condition):
        """
            在可迭代对象中，查找满足条件的单个元素。
        :param iterable_target:可迭代对象
        :param func_condition:所有条件
        :return:元素
        """
        for item in iterable_target:
            if func_condition(item):
                return item

    @staticmethod
    def find_total(iterable_target, func_condition):
        """
            在可迭代对象中，根据条件求和。
        :param iterable_target:可迭代对象
        :param func_condition:求和条件
        :return: 和的值
        """
        a = 0
        for item in iterable_target:
            a +=func_condition(item)
        return a

    @staticmethod
    def find_name(iterable_target, func_condition):
        """
            在可迭代对象中，选择满足条件的属性。
        :param iterable_target:可迭代对象
        :param func_condition:所有条件
        :return:生成器对象
        """
        for item in iterable_target:
                yield func_condition(item)

    @staticmethod
    def get_max(iterable_target, func_condition):
        """
            在可迭代对象中，查找最大值的元素。
        :param iterable_target:可迭代对象
        :param func_condition:值的条件
        :return:元素
        """
        max_num = iterable_target[0]
        for item in range(1,len(iterable_target)):
            if func_condition(max_num) < func_condition(iterable_target[item]):
                max_num = iterable_target[item]
        return max_num

    @staticmethod
    def order_up(iterable_target, func_condition):
        """
            在可迭代对象中，按条件进行升序排列。
        :param iterable_target:可迭代对象
        :param func_condition:条件
        :return:排序后的列表
        """
        for i in range(len(iterable_target)-1):
            for j in range(i+1,len(iterable_target)):
                if func_condition(iterable_target[i]) > func_condition(iterable_target[j]):
                    iterable_target[i],iterable_target[j]=iterable_target[j],iterable_target[i]

    @staticmethod
    def get_min(iterable_target, func_condition):
        """
            在可迭代对象中，查找最小值的元素。
        :param iterable_target:可迭代对象
        :param func_condition:值的条件
        :return:元素
        """
        min_num = iterable_target[0]
        for item in range(1,len(iterable_target)):
            if func_condition(min_num) > func_condition(iterable_target[item]):
                min_num = iterable_target[item]
        return min_num

    @staticmethod
    def order_down(iterable_target, func_condition):
        """
            在可迭代对象中，按条件进行降序排列。
        :param iterable_target:可迭代对象
        :param func_condition:条件
        :return:
        """
        for i in range(len(iterable_target) - 1):
            for j in range(i + 1, len(iterable_target)):
                if func_condition(iterable_target[i]) < func_condition(iterable_target[j]):
                    iterable_target[i], iterable_target[j] = iterable_target[j], iterable_target[i]

    @staticmethod
    def delete(iterable_target, func_condition):
        """
            在可迭代对象中，按条件进行降序排列。
        :param iterable_target:可迭代对象
        :param func_condition:条件
        :return:
        """
        for i in range(len(iterable_target) - 1,-1,-1):
            if func_condition(iterable_target[i]):
                del iterable_target[i]
