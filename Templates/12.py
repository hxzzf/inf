st = ''

while '' in st or ' ' in st:
    if ' ' in st:
        st = st.replace(' ', '', 1)
    if '' in st:
        st = st.replace('', '', 1)