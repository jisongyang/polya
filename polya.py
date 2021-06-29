from sympy import expand,Symbol

class Polyhedron():
    def __init__(self,polyhedron_name,aim):
        aim_dict={'顶点':'vertice','棱':'edge','面':'surface'}
        polyhedron_name_dict={'正四面体':'regular_tetrahedro',
                              '正六面体':'regular_hexahedro',
                              '正八面体':'regular_octahedro'}

        self.polyhedron_name=polyhedron_name_dict[polyhedron_name]
        self.aim=aim_dict[aim]
        if(self.polyhedron_name=='regular_tetrahedro'):
            self.regular_tetrahedro()
        if(self.polyhedron_name=='regular_hexahedro'):
            self.regular_hexahedro()
        if(self.polyhedron_name=='regular_octahedro'):
            self.regular_octahedro()
        self.info={'regular_tetrahedro':[4,6,4],'regular_hexahedro':[8,12,6],'regular_octahedro':[6,12,8]}

    def get_info(self):
        return self.info[self.polyhedron_name]

    ## 正四面体
    def regular_tetrahedro(self):
        ## 4个顶点置换群以及个数
        if (self.aim == 'vertice'):
            self.permutation_group = ['(1)1_(3)1:8', '(2)2:3', '(1)4:1']
            self.permutation_group_num = 12
            self.object_num = 4
        ## 6条边置换群以及个数
        if (self.aim == 'edge'):
            self.permutation_group = ['(3)2:8', '(1)2_(2)2:3', '(1)6:1']
            self.permutation_group_num = 12
            self.object_num = 6
        ## 6个面置换群以及个数
        if (self.aim == 'surface'):
            self.permutation_group = ['(1)1_(3)1:8', '(2)2:3', '(1)4:1']
            self.permutation_group_num = 12
            self.object_num = 4

    ## 正六面体
    def regular_hexahedro(self):
        ## 8个顶点置换群以及个数
        if(self.aim=='vertice'):
            self.permutation_group=['(1)2_(3)2:8','(2)4:6','(4)2:6','(2)4:3','(1)8:1']
            self.permutation_group_num=24
            self.object_num=8
        ## 12条边置换群以及个数
        if(self.aim=='edge'):
            self.permutation_group=['(3)4:8','(1)2_(2)5:6','(4)3:6','(2)6:3','(1)12:1']
            self.permutation_group_num = 24
            self.object_num = 12
        ## 6个面置换群以及个数
        if(self.aim=='surface'):
            self.permutation_group=['(3)2:8','(2)3:6','(1)2_(4)1:6','(1)2_(2)2:3','(1)6:1']
            self.permutation_group_num = 24
            self.object_num = 6

    ## 正八面体
    def regular_octahedro(self):
        ## 6个顶点置换群以及个数
        if(self.aim=='vertice'):
            self.permutation_group=['(1)2_(4)1:6','(1)2_(2)2:3','(2)3:6','(3)2:8','(1)6:1']
            self.permutation_group_num=24
            self.object_num=6
        ## 12条边置换群以及个数
        if(self.aim=='edge'):
            self.permutation_group=['(4)3:6','(2)6:3','(1)2_(2)5:6','(3)4:8','(1)12:1']
            self.permutation_group_num = 24
            self.object_num = 12
        ## 8个面置换群以及个数
        if(self.aim=='surface'):
            self.permutation_group=['(4)2:6','(2)4:3','(2)4:6','(1)2_(3)2:8','(1)8:1']
            self.permutation_group_num = 24
            self.object_num = 8

    ## 获取三种颜色染色的多项式
    def get_rbw_Polynomial(self):
        r = Symbol('r')
        b = Symbol('b')
        w = Symbol('w')
        Polynomial=0
        for group in self.permutation_group:
            this_Polynomial = 1
            group_num=int(group.split(':')[-1])
            state_list=group.split(':')[0].split('_')
            for state in state_list:
                [each_symbol_exp,sum_symbol_exp]=state[1:].split(')')
                m=int(each_symbol_exp)
                n=int(sum_symbol_exp)
                this_Polynomial=expand(this_Polynomial*(r**m+b**m+w**m)**n)
            Polynomial=expand(Polynomial+group_num*this_Polynomial)
        self.rbw_Polynomial=expand(Polynomial/self.permutation_group_num)

    ## 获取三种颜色染色的方案数
    def get_rbw_kinds(self,r_num,b_num,w_num=-1):
        self.get_rbw_Polynomial()
        if(w_num==-1):
            w_num=self.object_num-r_num-b_num
            if(w_num<0 ):
                return 0
        else:
            if(r_num+b_num+w_num!=self.object_num):
                return 0

        num_list=[str(r_num),str(b_num),str(w_num)]
        str_list=['r','b', 'w']
        for i in range(3):
            if(num_list[i]=='0'):
                str_list[i]=''
            elif(num_list[i]!='1'):
                str_list[i]=str_list[i]+'**'+num_list[i]
        [r_str,b_str,w_str]=str_list

        x_list = ''.join(str(self.rbw_Polynomial).split())
        x_list = str(x_list).split('+', -1)

        for item in x_list:
            if(r_str in item and b_str in item and w_str in item):
                # print(item)
                item_list=item.split('*')
                if(item_list[0] not in ['r','b','w']):
                    return int(item_list[0])
                else:
                    return 1
        return 0

    def get_all_kinds_by_color(self,color_num):
        all_kinds=0
        for group in self.permutation_group:
            this_kinds = 1
            group_num=int(group.split(':')[-1])
            state_list=group.split(':')[0].split('_')
            for state in state_list:
                [each_symbol_exp,sum_symbol_exp]=state[1:].split(')')
                m=int(each_symbol_exp)
                n=int(sum_symbol_exp)
                this_kinds=expand(this_kinds*(color_num)**n)
            all_kinds= expand(all_kinds + group_num * this_kinds)
        self.all_kinds = expand(all_kinds / self.permutation_group_num)
        return self.all_kinds

if __name__=='__main__':

    polyhedron=Polyhedron('正四面体','顶点')
    # polyhedron.get_rbw_Polynomial()
    #
    # print(polyhedron.get_rbw_kinds(9, 0))
    # print(polyhedron.get_rbw_kinds(8, 0))
    # print(polyhedron.get_rbw_kinds(7, 0))
    # print(polyhedron.get_rbw_kinds(6,0))
    # print(polyhedron.get_rbw_kinds(5,0))
    # print(polyhedron.get_rbw_kinds(4, 0))
    # print(polyhedron.get_rbw_kinds(3, 0))
    # print(polyhedron.get_rbw_kinds(2, 0))
    # print(polyhedron.get_rbw_kinds(1, 0))
    # print(polyhedron.get_rbw_kinds(0, 0,6))

    print(polyhedron.get_all_kinds_by_color(2))