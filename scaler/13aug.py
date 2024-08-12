# # def odd_even_split_tuple(tup):
# #     ''' input:tup-indicates the tuple
# #          output:print two tuples one for even indexed and odd indexed in the given output format'''
# #
# #     # YOUR CODE GOES HERE
# #     odd = ()
# #     even = ()
# #     tuple = ()
# #     result_even = ()
# #     result_odd = ()
# #
# #     for i in range(len(tup)):
# #         if i % 2 == 0:
# #             result_even += (tup[i],)
# #         else:
# #             result_odd += (tup[i],)
# #     print(f"{result_odd}")
# #     print(f"{result_even}")
# #
# #
# # tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
# #
# # odd_even_split_tuple(tup)
# # name_lst = ["Vijay", "Vickey"]
# # tup = ("Item_1", 0.5, name_lst)
# # name_lst.append("Vishal")
# # print(tup)
# tuple1 = (1150, 'sea_level', 909)
# print(max(tuple1))
#
# # tuple1 = (1150, 877, 909)
# # print(max(tuple1))
# #
# # tuple1[0] = 50
# # print(tuple[0])
def set_operation(sent1, sent2):
    com_set = sent1.union(sent2)
    unique_word = len(com_set)
    return unique_word


sent1 = {'use', 'process', 'create', 'better', 'analysis', 'in', 'it', 'further', 'and', 'we', 'data', 'interpreted',
         'to'}
sent2 = {'collected', 'more', 'be', 'and', 'data', 'passively', 'will'}
print(set_operation(sent1, sent2))
