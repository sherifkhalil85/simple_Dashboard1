
import streamlit as st
import plotly.express as px


st.set_page_config(
    layout="wide",
    page_title="Simple Dashboard"
)
df= px.data.tips()

# side bar
x= st.sidebar.checkbox('Show Data', False, key=1)
day= st.sidebar.selectbox('Select day', df['day'].unique())
time= st.sidebar.selectbox('Select Meal Time', df['time'].unique())

size= st.sidebar.radio("Select how many Dishes", sorted(df['size'].unique()),5, horizontal=True)

if x:
    st.header('Dataset Sample')
    st.dataframe(df.head(8))
# page content 
col1, col2, col3 = st.columns([5,2,5])

with col1:
    new_df1 = df[df['day'] == day]
    fig = px.histogram(new_df1, x = 'total_bill', color = 'sex',
                       title=f'totalt bill for {day}day'.title(), width = 700)
    st.plotly_chart(fig,use_container_width=True)
    new_df1 = df[df['size'] == size]
    fig = px.pie(new_df1, names = 'time', color = 'sex',
                 title=f'count of each meal time according to {size} dishes'.title()).update_traces(textinfo='value')
    st.plotly_chart(fig,use_container_width=True)
with col3:
    new_df2= df[df['time']== time]
    fig = px.scatter(new_df2, x='total_bill', y= 'tip',size='size',template="presentation",
                     size_max=20, color='sex', title=f'correlation between total bill and tip on {time}')
    st.plotly_chart(fig,use_container_width=True)
    fig= px.sunburst(df, path=['day', 'time'], color= 'tip', 
                    title= 'counting over day, time and size over tips'.title()).update_traces(textinfo='value')
    st.plotly_chart(fig, use_container_width=True)
