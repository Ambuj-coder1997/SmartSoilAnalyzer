import streamlit as st
import pickle
import numpy as np
from PIL import Image
image = Image.open('logo.jpg')

import streamlit as st

def load_model1():
    with open('mc1.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model1()
regressor1 = data["model3"]

def load_model2():
    with open('bd.pkl', 'rb') as file:
        data1 = pickle.load(file)
    return data1


data1 = load_model2()
regressor2 = data1["model4"]

def load_model3():
    with open('whc.pkl', 'rb') as file:
        data2 = pickle.load(file)
    return data2


data2 = load_model3()
regressor3 = data2["model5"]

def load_model4():
    with open('pH.pkl', 'rb') as file:
        data3 = pickle.load(file)
    return data3


data3 = load_model4()
regressor4 = data3["model6"]

def load_model5():
    with open('EC.pkl', 'rb') as file:
        data4 = pickle.load(file)
    return data4


data4 = load_model5()
regressor5 = data4["model7"]

def load_model6():
    with open('OC.pkl', 'rb') as file:
        data5 = pickle.load(file)
    return data5


data5 = load_model6()
regressor6 = data5["model8"]

def load_model7():
    with open('N.pkl', 'rb') as file:
        data6 = pickle.load(file)
    return data6


data6 = load_model7()
regressor7 = data6["model9"]

def load_model8():
    with open('P.pkl', 'rb') as file:
        data7 = pickle.load(file)
    return data7


data7 = load_model8()
regressor8 = data7["model10"]

def load_model9():
    with open('K.pkl', 'rb') as file:
        data8 = pickle.load(file)
    return data8


data8 = load_model9()
regressor9 = data8["model11"]

def load_model10():
    with open('Ca.pkl', 'rb') as file:
        data9 = pickle.load(file)
    return data9


data9 = load_model10()
regressor10 = data9["model12"]

def load_model11():
    with open('Mg.pkl', 'rb') as file:
        data10 = pickle.load(file)
    return data10


data10 = load_model11()
regressor11 = data10["model13"]

def load_model12():
    with open('S.pkl', 'rb') as file:
        data11 = pickle.load(file)
    return data11


data11 = load_model12()
regressor12 = data11["model14"]

def load_model13():
    with open('Fe.pkl', 'rb') as file:
        data12 = pickle.load(file)
    return data12


data12 = load_model13()
regressor13 = data12["model15"]

def load_model14():
    with open('Mn.pkl', 'rb') as file:
        data13 = pickle.load(file)
    return data13


data13 = load_model14()
regressor14 = data13["model16"]

def load_model15():
    with open('Cu.pkl', 'rb') as file:
        data14 = pickle.load(file)
    return data14


data14 = load_model15()
regressor15 = data14["model17"]

def load_model16():
    with open('Zn.pkl', 'rb') as file:
        data15 = pickle.load(file)
    return data15


data15 = load_model16()
regressor16 = data15["model18"]


def show_predict_page():
    #st.title("PaddyProOptimizer : Web Application for Physio-chemical Properties Prediction of Soil mix with Vermicompost and Farmyard Manure")
    st.title("SmartSoilAnalyzer: Android App for Predicting Soil Physiochemical Properties mix with Vermicompost and Farmyard Manure ")
    st.sidebar.image(image, use_column_width=True)
    st.write("""### We need some information regarding treatment proportions to predict the physical and chemical properties of soil organic growing media:""")

    VC = st.number_input('Enter Vermicompost proportion (%) in treatment combination')
    FYM = st.number_input('Enter Farmyard Manure proportion (%) in treatment combination')
    Soil = st.number_input('Enter Soil proportion (%) in treatment combination')

    ok = st.button("Predict Physical Properties")
    if ok:
        X1 = np.array([[VC, FYM, Soil]])
        X1 = X1.astype(float)
        salary1 = regressor1.predict(X1)
        st.subheader(f"The Moisture Content (%) is {salary1[0]:.2f}")
        X2 = np.array([[VC, FYM, Soil]])
        X2 = X2.astype(float)
        salary2 = regressor2.predict(X2)
        st.subheader(f"The Bulk Density (g/cm3) is {salary2[0]:.2f}")
        X3 = np.array([[VC, FYM, Soil]])
        X3 = X3.astype(float)
        salary3 = regressor3.predict(X3)
        st.subheader(f"The Water Holding Capacity (%) is {salary3[0]:.2f}")

    ok2 = st.button("Predict Chemical Properties")
    if ok2:
        X4 = np.array([[VC, FYM, Soil]])
        X4 = X4.astype(float)
        salary4 = regressor4.predict(X4)
        st.subheader(f"The pH value is {salary4[0]:.2f}")
        X5 = np.array([[VC, FYM, Soil]])
        X5 = X5.astype(float)
        salary5 = regressor5.predict(X5)
        st.subheader(f"The Electrical Conductivity (dS/m) value is {salary5[0]:.2f}")
        X6 = np.array([[VC, FYM, Soil]])
        X6 = X6.astype(float)
        salary6 = regressor6.predict(X6)
        st.subheader(f"The Organic Carbon (%) value is {salary6[0]:.2f}")
        X7 = np.array([[VC, FYM, Soil]])
        X7 = X7.astype(float)
        salary7 = regressor7.predict(X7)
        st.subheader(f"Macronutrients:")
        st.subheader(f"The Nitrogen (%) value is {salary7[0]:.2f}")
        X8 = np.array([[VC, FYM, Soil]])
        X8 = X8.astype(float)
        salary8 = regressor8.predict(X8)
        st.subheader(f"The Phosphorus (%) value is {salary8[0]:.2f}")
        X9 = np.array([[VC, FYM, Soil]])
        X9 = X9.astype(float)
        salary9 = regressor9.predict(X9)
        st.subheader(f"The Potassium (%) value is {salary9[0]:.2f}")
        X10 = np.array([[VC, FYM, Soil]])
        X10 = X10.astype(float)
        salary10 = regressor10.predict(X10)
        st.subheader(f"Micronutrients:")
        st.subheader(f"The Calcium (mg/kg) value is {salary10[0]:.2f}")
        X11 = np.array([[VC, FYM, Soil]])
        X11 = X11.astype(float)
        salary11 = regressor11.predict(X11)
        st.subheader(f"The Magnesium (mg/kg) value is {salary11[0]:.2f}")
        X12 = np.array([[VC, FYM, Soil]])
        X12 = X12.astype(float)
        salary12 = regressor12.predict(X12)
        st.subheader(f"The Sulphur (mg/kg) value is {salary12[0]:.2f}")
        X13 = np.array([[VC, FYM, Soil]])
        X13 = X13.astype(float)
        salary13 = regressor13.predict(X13)
        st.subheader(f"The Iron (mg/kg) value is {salary13[0]:.2f}")
        X14 = np.array([[VC, FYM, Soil]])
        X14 = X14.astype(float)
        salary14 = regressor14.predict(X14)
        st.subheader(f"The Manganese (mg/kg) value is {salary14[0]:.2f}")
        X15 = np.array([[VC, FYM, Soil]])
        X15 = X15.astype(float)
        salary15 = regressor15.predict(X15)
        st.subheader(f"The Copper (mg/kg) value is {salary15[0]:.2f}")
        X16 = np.array([[VC, FYM, Soil]])
        X16 = X16.astype(float)
        salary16 = regressor16.predict(X16)
        st.subheader(f"The Zinc (mg/kg) value is {salary16[0]:.2f}")


