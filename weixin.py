#coding:gbk
"""
����Ŀ��:���RPSLSС��Ϸ
���ߣ��
����2021/06/07
"""
print("��ӭ����RPSLS��Ϸ")
print("----------------")
print("ʯͷ/����/��/����/ʷ����")
player_choice = input("����������ѡ��:")
print(player_choice)  # ��ʾ������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
print("----------------")
choice_name = input()
if player_choice == 'ʯͷ':
    player_choice_number = 0      # ����name_to_number()�������û���ѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    print('����ѡ��Ϊ��ʯͷ')
elif player_choice == 'ʷ����':   # ����if/elif/else ��䣬���� RPSLS ������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    player_choice_number = 1
    print('����ѡ��Ϊ��ʷ����')
elif player_choice == '��':
    player_choice_number = 2
    print('����ѡ��Ϊ����')
elif player_choice == '����':
    player_choice_number = 3
    print('����ѡ��Ϊ������')
elif player_choice == '����':
    player_choice_number = 4
    print('����ѡ��Ϊ������')
else:
    print('Error: No Correct Name')

from random import randrange       # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
comp_number = int(randrange(0,4))    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
if comp_number == 0:
    print('�������ѡ��Ϊ��ʯͷ')      # ����Ļ����ʾ�����ѡ����������
if comp_number == 1:
    print('�������ѡ��Ϊ��ʷ����')
if comp_number == 2:
    print('�������ѡ��Ϊ����')
if comp_number == 3:
    print('�������ѡ��Ϊ������')
if comp_number == 4:
    print('�������ѡ��Ϊ������')

# ����û��ͼ����ѡ����ͬ������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
if player_choice_number != comp_number:
    if player_choice_number > comp_number:
        print("��Ӯ��")
    elif player_choice_number < comp_number:
        print("�����Ӯ��")
else:
    print('���ͼ��������һ����')
