#я так поняла, что 6 задание должно включать 7-ое:
def int_func():
    while True:
        st = input('words: ')
        if st.isupper() or st.istitle():
            print('only lower')
        elif st.islower():
            print(st.title())
        if st.isalnum():
            break
int_func()

