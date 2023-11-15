# Streamlit frontend
import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql
import pandas as pd
import plotly.express as px

# DataBase connection 
Mydb = sql.connect(host = "localhost",
                   user = "root",
                   password = "your password",
                   database = "phonepe")
mycursor = Mydb.cursor(buffered=True)

# streamlit webpage design
st.set_page_config(page_title= "Phonepe",
                   page_icon= "https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/phonepe-logo-icon.png",
                   layout= "wide")
st.sidebar.header(":wave: :violet[**Hello! Welcome to the dashboard**]")
page_bg_img = """
<style>
body {
    background-image: url("https://cdn.pixabay.com/photo/2014/06/16/23/39/black-370118_640.png");
    background-size: cover;
}
[data-testid="stAppViewContainer"] {
    background-image: url("https://cdn.pixabay.com/photo/2014/06/16/23/39/black-370118_640.png");
    background-size: cover;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
[data-testid="stToolbar"] {
    right: 5rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("data:image/png;base64");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit sidebar design
with st.sidebar:
    selected = option_menu("Menu", ["Home","Top Charts","Explore Data","My-Profile"], 
                icons=["house","graph-up-arrow","bar-chart-line", "list-task"],
                menu_icon= "menu-button-wide",
                default_index=0,
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#9a78eb"},
                        "nav-link-selected": {"background-color": "#5d78a3"}})

# Home design Description
if selected == "Home":
    st.markdown("# :rainbow[Data Visualization and Exploration]")
    st.markdown("## :grey[A User-Friendly Tool Using Streamlit and Plotly]")
    col1,col2 = st.columns([3,2],gap="medium")
    with col1:
        st.markdown("### :grey[Technologies used : ]:blue[Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.]")
        st.markdown("### :grey[Overview : ]:blue[In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.]")
        st.write(" ")
        st.write(" ")
        st.image("27736-temp-02-2-2.png")
        
if selected == "Top Charts":
    st.markdown("## :green[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year=st.selectbox('**Year**',('2018','2019','2020','2021','2022'))
        Quarter=st.selectbox('**Quarter**',('1','2','3','4'))
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
    
    if Type == "Transactions":
        col1,col2,col3 = st.columns([1,1,1],gap="small")
        
        with col1:
            st.markdown("### :green[Top 10 State]")
            mycursor.execute(f"select State, sum(Transaction_count) AS Total_Transactions_Count,sum(Transaction_amount) AS Total from aggregated_trans where Year = {Year} AND Quarter = {Quarter} group by State order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Transactions_Count', 'Total']) #------ to change in 'total amount' - total 
            fig = px.pie(df, values='Total',
                             names='State',
                            #  title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Viridis,
                             hover_data=['Total_Transactions_Count'],
                             labels={'Total_Transactions_Count':'Total_Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :green[Top 10 District]")
            mycursor.execute(f"select District , sum(Count) as Total_Count, sum(Amount) as Total from map_trans where Year = {Year} and Quarter = {Quarter} group by District order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Count','Total'])

            fig = px.pie(df, values='Total',
                             names='District',
                            #  title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['Total_Count'],
                             labels={'Total_Count':'Total_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col3:
            st.markdown("### :green[Top 10 Pincode]")
            mycursor.execute(f"select Pincode, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_Amount) as Total from top_trans where Year = {Year} and  Quarter= {Quarter} group by Pincode  order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Total_Transactions_Count','Total'])
            fig = px.pie(df, values='Total',
                             names='Pincode',
                            #  title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Viridis,
                             hover_data=['Total_Transactions_Count'],
                             labels={'Total_Transactions_Count':'Total_Transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)    
# --------------------------------------------------------------------------------------
    if Type == "Users":
        col1,col2,col3,col4 = st.columns([2,2,2,2],gap="small")
        
        with col1:
            st.markdown("### :green[Brands]")
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                mycursor.execute(f"select Brands, SUM(Count) as total_user_count, AVG(Percentage) * 100 as avg_user_percentage from aggregate_user where Year = {Year} and Quarter = {Quarter} group by Brands order by total_user_count desc limit 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Brands', 'total_user_count', 'avg_user_percentage'])

                import plotly.express as px
                fig = px.bar(
                    df,
                    title='Top 10 User Brands',
                    x="total_user_count",
                    y="Brands",
                    orientation='h',
                    color='avg_user_percentage',
                    color_discrete_sequence=px.colors.sequential.Viridis)

                fig.update_layout(xaxis_title='Total User Count', yaxis_title='User Brand')
                st.plotly_chart(fig, use_container_width=True)
   
    
        with col2:
            st.markdown("### :green[District]")
            mycursor.execute(f"select District, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Year = {Year} and Quarter= {Quarter} group by District,RegisteredUser order by Total_Users  desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'registered_user','app_opens'])
            df.registered_user = df.registered_user.astype(float)
            fig = px.bar(df,
                         title='Top 10',
                         x="registered_user",
                         y="District",
                         orientation='h',
                         color='registered_user',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
              
        with col3:
            st.markdown("### :green[Pincode]")
            mycursor.execute(f"select Pincode, sum(RegisteredUsers) as Total_Users from top_user where Year = {Year} and Quarter= {Quarter} group by Pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'registered_user'])
            fig = px.pie(df,
                         values='registered_user',
                         names='Pincode',
                         title='Top 10',
                         color_discrete_sequence=px.colors.sequential.Viridis,
                         hover_data=['registered_user'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :green[State]")
            mycursor.execute(f"select State, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Year = {Year} and Quarter= {Quarter} group by State order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'registered_user','app_opens'])
            fig = px.pie(df, values='registered_user',
                             names='State',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['app_opens'],
                             labels={'app_opens':'app_opens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

if selected == "Explore Data":
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2022)
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
    
    col1,col2= st.columns(2)   
     #EXPLORE DATA - Transactions   
    if Type == "Transactions":     
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        with col1:
            st.markdown("## :violet[Overall State Data - Transactions Amount]")
            mycursor.execute(f"select State, sum(Count) as Total_Transactions, sum(Amount) as Total_amount from map_trans where Year = {Year} and Quarter= {Quarter} group by State order by State")
            df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            df2 = pd.read_csv('state_names.csv')
            # df1.transaction_amount = df1.transaction_amount.astype(int )
            df1['state'] = df2['state']
            
            
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='Total_amount',
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
            
            with col2:
                st.markdown("## :violet[Overall State Data - Transactions count]")
                mycursor.execute(f"select State, sum(Count) as Total_Transactions, sum(Amount) as Total_amount from map_trans where Year = {Year} and Quarter= {Quarter} group by State order by State")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv('state_names.csv')
                # df1.transaction_count = df1.transaction_count.astype(int )
                df1['state'] = df2['state']
                
                
                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='state',
                            color='Total_Transactions',
                            color_continuous_scale='sunset')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
                
            with col1:   
                # BAR CHART - TOP PAYMENT TYPE
                st.markdown("## :violet[Top Payment Type]")
                mycursor.execute(f"select Transaction_type, sum(Transaction_count) as Total_Transactions_count, sum(Transaction_amount) as Total_Transactions_amount from aggregated_trans where Year= {Year} and Quarter = {Quarter} group by Transaction_type order by Transaction_type")
                df = pd.DataFrame(mycursor.fetchall(), columns=['Transaction_type', 'Total_Transactions_count','Total_Transactions_amount'])

                fig = px.bar(df,
                            title='Transaction Types vs Total_Transactions',
                            x="Transaction_type",
                            y="Total_Transactions_count",
                            orientation='v',
                            color='Total_Transactions_amount',
                            color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=False) 
            with col2:
                # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
                st.markdown("## :violet[Select any State to explore more]")
                selected_state = st.selectbox("",
                                    ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                    'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                    'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                    'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                    'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                    'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)
                
                mycursor.execute(f"select State, District,Year,Quarter, sum(Count) as Total_Transactions_count, sum(Amount) as Total_transaction_amount from map_trans where Year = {Year} and Quarter = {Quarter} and State = '{selected_state}' group by State, District,Year,Quarter order by State,District")
                
                df1 = pd.DataFrame(mycursor.fetchall(), columns=['State','District','Year','Quarter',
                                                                'Total_Transactions_count','Total_transaction_amount'])
                fig = px.bar(df1,
                            title=selected_state,
                            x="District",
                            y="Total_Transactions_count",
                            orientation='v',
                            color='Total_transaction_amount',
                            color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)

#  ------------    -------------------------------
    if Type == "Users":
        # Overall State Data - User App Opening Frequency
        st.markdown("## :violet[Overall State Data - User App Opening Frequency]")
        mycursor.execute(f"SELECT State, SUM(RegisteredUser) AS Total_Users, SUM(AppOpens) AS Total_Appopens FROM map_user WHERE Year = {Year} AND Quarter = {Quarter} GROUP BY State ORDER BY State")
        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users', 'Total_Appopens'])
        df2 = pd.read_csv('state_names.csv')  # Assuming you have a CSV file with state names
        df1['Total_Appopens'] = df1['Total_Appopens'].astype(float)
        df1['state'] = df2['state']

        fig = px.choropleth(
            df1,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='state',
            color='Total_Appopens',
            color_continuous_scale='sunset'
        )
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

        # BAR CHART TOTAL USERS - DISTRICT WISE DATA
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox(
            "",
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
            'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat', 'haryana',
            'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
            'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
            'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'), index=30)

        mycursor.execute(
            f"SELECT State, Year, Quarter, District, SUM(RegisteredUser) AS Total_Users, SUM(AppOpens) AS Total_Appopens FROM map_user WHERE Year = {Year} AND Quarter = {Quarter} AND State = '{selected_state}' GROUP BY State, District, Year, Quarter ORDER BY State, District")

        df = pd.DataFrame(mycursor.fetchall(),
                        columns=['State', 'Year', 'Quarter', 'District', 'Total_Users', 'Total_Appopens'])
        df.Total_Users = df.Total_Users.astype(int)

        fig = px.bar(df,
                    title=selected_state,
                    x="District",
                    y="Total_Users",
                    orientation='v',
                    color='Total_Users',
                    color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig, use_container_width=True)


if selected == "My-Profile":
    col1,col2 = st.columns([3,3],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.subheader(":white[Phone Pulse: ]",divider='rainbow')
