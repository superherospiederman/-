#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2021.12.2
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif naem=="����":
        return 4
    else:
        print("����")

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��





def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return"ʯͷ"
    elif number==1:
        return"ʷ����"
    elif number==2:
        return"ֽ"
    elif number==3:
        return"����"
    elif number==4:
        return"����"
    else:
        print("����")


    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("-------- ")
    print("���ѡ�����Ϊ%s"%choice_name)
    player_choice_number=name_to_number(choice_name)
    comp_number=random.randrange(0,4)
    comp_number_name=number_to_name(comp_number)
    print("�������ѡ�����Ϊ%s"%comp_number_name)
    if player_choice_number==comp_number:
        print("��ͼ��������һ����")
    elif comp_number==0 and  player_choice_number==1 or 2:
        print("��Ӯ��")
    elif comp_number==1 and  player_choice_number==2 or 3 :
        print("��Ӯ��")
    elif comp_number == 2 and player_choice_number == 4 or 3:
        print("��Ӯ��")
    elif comp_number==3 and  player_choice_number==0 or 4:
        print("��Ӯ��")
    elif comp_number==4 and  player_choice_number==0 or 1:
        print("��Ӯ��")
    else:
        print("�����Ӯ��")



    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬ayer_choice�������pl

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


