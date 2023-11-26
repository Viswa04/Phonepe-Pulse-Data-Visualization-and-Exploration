import json
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import PIL
from PIL import Image
import psycopg2

# SQL Connection
mydb = psycopg2.connect(host = "localhost",
                        user = "postgres",
                        password = "Viswa@04",
                        database = "Phonepe_pulse",
                        port = "5432")

cursor = mydb.cursor()



st.set_page_config(page_title = "Phonepe",
                    layout = "wide")

tab1,tab2,tab3 = st.tabs(["***HOME***","***EXPLORE DATA***","***TOP CHARTS***"])

with tab1:
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open("C:/Users/user/Desktop/Phonepe/Phonepe.png"),width=500)
    with col2:
        st.image(Image.open("C:/Users/user/Desktop/Phonepe/Phonepe_2.png"),width=600)
    st.header(":red[Phonepe]")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader(":red[Introduction]")
        st.markdown("_PhonePe is a India's Payment App. It is a mobile payment platform using which you can transfer money using UPI, recharge phone numbers, pay utility bills, etc. PhonePe works on the Unified Payment Interface (UPI) system and all you need is to feed in your bank account details and create a UPI ID._")
        st.markdown("_The PhonePe app is available in 11 Indian languages. Using PhonePe, users can send and receive money, recharge mobile, DTH, data cards, make utility payments, pay at shops, invest in tax saving funds, buy insurance, mutual funds, and digital gold_")
        st.markdown("_PhonePe is accepted as a payment option by over 3.6 crore offline and online merchant outlets, constituting 99% of pin codes in the country. The app served more than 10 crore users as of June 2018,processed 500 crore transactions by December 2019,and crossed 10 crore transactions a day in April 2022.  It currently has over 50 crore registered users with over 20 crore monthly active users._")
    with col2:
        st.video("https://youtu.be/aXnNA4mv1dU?si=jbRNEUTgFztl9upY")
    
    st.header(":red[Phonepe Pulse]")
    col1,col2 = st.columns(2)
    with col1:
        st.image(Image.open("C:/Users/user/Desktop/Phonepe/Phonepe_Pulse_1.png"),width=500)
        st.subheader(":red[Introduction]")
        st.markdown("_The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government. Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. PhonePe Pulse is our way of giving back to the digital payments ecosystem._")
    with col2:
        st.video("https://youtu.be/c_1H6vivsiA?si=1EawZboKvkWDiAfX")

    st.header(":red[Download the App]")
    st.link_button("Get Phonepe App","https://www.phonepe.com/app-download/")

with tab3:
    question = st.selectbox("Select the question",("None","1. Top 10 Mobile brands based on Transaction count","2. Top 10 States based on year and transaction amount",
                                                    "3. Top 10 States based on users registered","4. Top 10 Districts based on users registered",
                                                    "5. Top 10 Districts with least transaction amount","6. Top 10 States with App opens",
                                                    "7. Top Transaction type based on transaction amount","8. Top 15 States based on transaction count",
                                                    "9. Top 10 Districts with highest transaction amount","10. Total Transaction count in 6 years"))

    if question == "1. Top 10 Mobile brands based on Transaction count":
        query1 = "select brands as Mobile_Brands,sum(transaction_count) as No_of_Transaction from aggregated_user group by brands order by No_of_Transaction desc limit 10"
        cursor.execute(query1)
        mydb.commit()
        data1 = cursor.fetchall()
        table1 = pd.DataFrame(data1, columns =["Mobile_Brands","No_of_Transaction"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table1)
        with col2:
            st.header("Pie chart for particular Table")
            fig,ax = plt.subplots()
            ax.pie(table1["No_of_Transaction"], labels=table1["Mobile_Brands"], autopct="%1.1f%%", startangle=45)
            ax.axis("equal")
            st.pyplot(fig)

    if question == "2. Top 10 States based on year and transaction amount":
        query2 = "select states,years,sum(transaction_amount) as Total_Transaction_amount from top_transaction group by states, years order by Total_Transaction_amount desc limit 10"
        cursor.execute(query2)
        mydb.commit()
        data2 = cursor.fetchall()
        table2 = pd.DataFrame(data2, columns = ["States","Years","Transaction_amount"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table2)
        with col2:
            st.header("Scatter Chart for particular Table")
            fig,ax = plt.subplots()
            scatter = ax.scatter(table2["States"], table2["Transaction_amount"], c=table2["Years"], label=table2["Years"])
            ax.legend(*scatter.legend_elements(), title="Years")
            ax.set_xticklabels(table2["States"], rotation=45, ha="right")
            ax.set_xlabel("States")
            ax.set_ylabel("Transaction_amount")
            st.pyplot(fig)
    
    if question == "3. Top 10 States based on users registered":
        query3 = "select states,years,sum(registered_users) as Total_users from top_user group by states,years order by Total_users desc limit 10"
        cursor.execute(query3)
        mydb.commit()
        data3 = cursor.fetchall()
        table3 = pd.DataFrame(data3, columns = ["States","Years","No.of Users"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table3)
        with col2:
            st.header("Pie chart for particular Table")
            fig,ax = plt.subplots()
            ax.pie(table3["No.of Users"], labels=table3["States"], autopct="%1.1f%%", startangle=90)
            ax.axis("equal")
            st.pyplot(fig)
    
    if question == "4. Top 10 Districts based on users registered":
        query4 = "select district, states, sum(registered_users) as Total_users from map_user group by district,states order by Total_users desc limit 10"
        cursor.execute(query4)
        mydb.commit()
        data4 = cursor.fetchall()
        table4 = pd.DataFrame(data4, columns = ["Districts","States","No.of Users"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table4)
        with col2:
            st.header("Scatter Chart for particular Table")
            fig,ax = plt.subplots()
            scatter = ax.scatter(table4["Districts"], table4["No.of Users"])
            ax.set_xticklabels(table4["Districts"], rotation=45, ha="right")
            ax.set_xlabel("Districts")
            ax.set_ylabel("No.of Users")
            st.pyplot(fig)
    
    if question == "5. Top 10 Districts with least transaction amount":
        query5 = "select district, sum(transaction_amount) as Total_Transaction from map_transaction group by district order by Total_Transaction asc limit 10"
        cursor.execute(query5)
        mydb.commit()
        data5 = cursor.fetchall()
        table5 = pd.DataFrame(data5, columns = ["Districts","Transaction_Amount"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table5)
        with col2:
            st.header("Bar Chart for particular Table")
            fig,ax = plt.subplots()
            ax.bar(table5["Districts"], table5["Transaction_Amount"])
            ax.set_xticklabels(table5["Districts"], rotation=45, ha="right")
            ax.set_xlabel("Districts")
            ax.set_ylabel("Transaction_Amount")
            st.pyplot(fig)
    
    if question == "6. Top 10 States with App opens":
        query6 = "select states, sum(app_opens) as app_opens from map_user group by states order by app_opens desc limit 10"
        cursor.execute(query6)
        mydb.commit()
        data6 = cursor.fetchall()
        table6 = pd.DataFrame(data6, columns=["States","App_Opens"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table6)
        with col2:
            st.header("Bar Chart for particular Table")
            fig,ax = plt.subplots()
            ax.bar(table6["States"], table6["App_Opens"])
            ax.set_xticklabels(table6["States"], rotation=45, ha="right")
            ax.set_xlabel("States")
            ax.set_ylabel("App_Opens")
            st.pyplot(fig)
    
    if question == "7. Top Transaction type based on transaction amount":
        query7 = "select transaction_type, sum(transaction_amount) as transaction_amount from aggregated_transaction group by transaction_type order by transaction_amount desc"
        cursor.execute(query7)
        mydb.commit()
        data7 = cursor.fetchall()
        table7 = pd.DataFrame(data7, columns=["Transaction_Type","Transaction_Amount"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table7)
        with col2:
            st.header("Line Chart for particular Table")
            fig,ax = plt.subplots()
            ax.plot(table7["Transaction_Type"], table7["Transaction_Amount"], marker="o")
            ax.set_xticklabels(table7["Transaction_Type"], rotation=45, ha="right")
            ax.set_xlabel("Transaction_Type")
            ax.set_ylabel("Transaction_Amount")
            st.pyplot(fig)
    
    if question == "8. Top 15 States based on transaction count":
        query8 = "select states, sum(transaction_count) as Total_Transaction from aggregated_transaction group by states order by Total_Transaction desc limit 15"
        cursor.execute(query8)
        mydb.commit()
        data8 = cursor.fetchall()
        table8 = pd.DataFrame(data8, columns=["States","Total_Transaction"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table8)
        with col2:
            st.header("Line Chart for particular Table")
            fig,ax = plt.subplots()
            ax.plot(table8["States"], table8["Total_Transaction"], marker="o")
            ax.set_xticklabels(table8["States"], rotation=45, ha="right")
            ax.set_xlabel("States")
            ax.set_ylabel("Total_Transaction")
            st.pyplot(fig)
    
    if question == "9. Top 10 Districts with highest transaction amount":
        query9 = "select district, sum(transaction_amount) as Total_Transaction from map_transaction group by district order by Total_Transaction desc limit 10"
        cursor.execute(query9)
        mydb.commit()
        data9 = cursor.fetchall()
        table9 = pd.DataFrame(data9, columns=["Districts","Transaction_Amount"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table9)
        with col2:
            st.header("Line Chart for particular Table")
            fig,ax = plt.subplots()
            ax.plot(table9["Districts"], table9["Transaction_Amount"], marker="o")
            ax.set_xticklabels(table9["Districts"], rotation=45, ha="right")
            ax.set_xlabel("Districts")
            ax.set_ylabel("Transaction_Amount")
            st.pyplot(fig)
    
    if question == "10. Total Transaction count in 6 years":
        query10 = "select years,sum(transaction_count) as Total_Transaction from aggregated_transaction group by years order by Total_Transaction desc"
        cursor.execute(query10)
        mydb.commit()
        data10 = cursor.fetchall()
        table10 = pd.DataFrame(data10, columns=["Years","No. of Transaction"])
        col1,col2 = st.columns(2)
        with col1:
            st.table(table10)
        with col2:
            st.header("Bar Chart for particular Table")
            fig,ax = plt.subplots()
            ax.bar(table10["Years"], table10["No. of Transaction"])
            ax.set_xlabel("Years")
            ax.set_ylabel("No. of Transaction")
            st.pyplot(fig)

with tab2:
    Type = st.selectbox("Select the Type",("Transactions","Users"))
    
    # Transaction Typer
    if Type == "Transactions":
        Selected_states = st.selectbox("Select the State",("Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh","Assam",
                                        "Bihar","Chandigarh","Chhattisgarh","Dadra And Nagar Haveli And Daman And Diu",
                                        "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand",
                                        "Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur",
                                        "Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
                                        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"))
        
        col1,col2 = st.columns(2)
        with col1:
            Year = st.selectbox("Select the year",("2018","2019","2020","2021","2022","2023"))

        with col2:
            Quarter = st.selectbox("Select the Quarter",("1","2","3","4"))
        
        with col1:
            # Geo Visualization of all States based on Transaction Amount
            st.subheader(":red[All States based on Transaction Amount]")
            query_1 = (f"select states, sum(transaction_count) as Total_Transaction,"
                        f"sum(transaction_amount) as Total_Amount from map_transaction where years={Year} and quarter={Quarter} group by states order by states")

            cursor.execute(query_1)
            mydb.commit()
            data_1 = cursor.fetchall()
            table_1 = pd.DataFrame(data_1,columns=["State","Total_Transaction","Total_Amount"])

            fig = px.choropleth(table_1, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='Total_Amount',
                                color_continuous_scale='Reds',
                                hover_name='State')
            
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Geo Visualization of all States based on Transaction Count
            st.subheader(":red[All States based on Transaction Count]")
            query_2 = (f"select states, sum(transaction_count) as Total_Transaction,"
                        f"sum(transaction_amount) as Total_Amount from map_transaction where years={Year} and quarter={Quarter} group by states order by states")

            cursor.execute(query_2)
            mydb.commit()
            data_2 = cursor.fetchall()
            table_2 = pd.DataFrame(data_2,columns=["State","Total_Transaction","Total_Amount"])

            fig = px.choropleth(table_2, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                featureidkey='properties.ST_NM',
                                locations='State',
                                color='Total_Transaction',
                                color_continuous_scale='Reds',
                                hover_name='State')
            
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)
        
        # Bar Chart for Transaction
        st.header(":red[Bar Chart for the particular filter]")
        query1 = (f"select states,years,quarter,district, sum(transaction_count) as Total_Transaction, "
                f"sum(transaction_amount) as Total_Amount from map_transaction where years={Year} and quarter={Quarter} and states='{Selected_states}' group by states,years,quarter,district order by states,district")
        
        cursor.execute(query1)
        mydb.commit()
        data1 = cursor.fetchall()
        table1 = pd.DataFrame(data1, columns=["State","Year","Quarter","District","Total_Transaction","Total_Amount"])
        st.markdown("# ")
        st.markdown("# ")
        st.markdown("# ")
        fig,ax = plt.subplots(figsize=(20,6))
        ax.bar(table1["District"], table1["Total_Transaction"])
        ax.set_xlabel("District")
        ax.set_ylabel("Total_Transaction")
        ax.set_xticklabels(table1["District"], rotation=45, ha="right")
        st.pyplot(fig)
    
    # Users Type
    if Type == "Users":
        Selected_states = st.selectbox("Select the State",("Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh","Assam",
                                        "Bihar","Chandigarh","Chhattisgarh","Dadra And Nagar Haveli And Daman And Diu",
                                        "Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand",
                                        "Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur",
                                        "Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim",
                                        "Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"))
        
        col1,col2 = st.columns(2)
        with col1:
            Year = st.selectbox("Select the year",("2018","2019","2020","2021","2022","2023"))
        with col2:
            Quarter = st.selectbox("Select the Quarter",("1","2","3","4"))

        # Geo Visualization of all States based on User App opens
        st.subheader(":red[All States based on User App opens]")
        query_3 = (f"select states, sum(registered_users) as Total_Users,"
                    f"sum(app_opens) as Total_Appopens from map_user where years={Year} and quarter={Quarter} group by states order by states")

        cursor.execute(query_3)
        mydb.commit()
        data_3 = cursor.fetchall()
        table_3 = pd.DataFrame(data_3,columns=["State","Total_Users","Total_Appopens"])

        fig = px.choropleth(table_3, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Users',
                            color_continuous_scale='rainbow',
                            hover_name='State')
        
        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Bar Chart for User
        st.header(":red[Bar Chart for the particular filter]")
        query2 = (f"select states,years,quarter,district, sum(registered_users) as Total_Users,"
                    f"sum(app_opens) as Total_Appopens from map_user where years={Year} and quarter={Quarter} and states='{Selected_states}' group by states,years,quarter,district order by states,district")
        
        cursor.execute(query2)
        mydb.commit()
        data2 = cursor.fetchall()
        table2 = pd.DataFrame(data2, columns=["State","Year","Quarter","District","Total_Users","Total_Appopens"])
        st.markdown("# ")
        st.markdown("# ")
        st.markdown("# ")
        fig,ax = plt.subplots(figsize=(20,6))
        ax.bar(table2["District"], table2["Total_Users"])
        ax.set_xlabel("District")
        ax.set_ylabel("Total_Users")
        ax.set_xticklabels(table2["District"], rotation=45, ha="right")
        st.pyplot(fig)




            


