import streamlit as st
view = [100,150,30,15,5,3]
st.write('# 나령 윤기도 Sample view')
st.write('## raw')
view
st.write('## bar chrt')
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview
