# coding=gbk
from MyQR import myqr
import os

version, level, qr_name = myqr.run(
    words="You're toast, man!!! ",  # �������ַ�����Ҳ��������ַ(ǰ��Ҫ��http(s)://)
    version=1,  # �����ݴ���Ϊ���
    level='H',  # ���ƾ���ˮƽ����Χ��L��M��Q��H����������������
    picture="hhh.png",  # ����ά���ͼƬ�ϳ�
    colorized=True,  # ��ɫ��ά��
    contrast=1.0,  # ���Ե���ͼƬ�ĶԱȶȣ�1.0 ��ʾԭʼͼƬ����С��ֵ��ʾ���ͶԱȶȣ�����֮��Ĭ��Ϊ1.0
    brightness=1.0,  # ��������ͼƬ�����ȣ������÷���ȡֵͬ��
    save_name="1.png",  # �����ļ������֣���ʽ������jpg,png,bmp,gif
    save_dir=os.getcwd()  # ����λ��
)
