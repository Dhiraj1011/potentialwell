
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Quantum Mechanics')
st.header('1-D Potential Well',divider='rainbow')

a=st.slider('Enter the length of well',1,20)
x=np.linspace(-a,a,10000)

def psi(x, n):
    y = np.sqrt(2 / a) * np.sin((n * np.pi * x) / (a))
    return y

n=st.slider('Enter the state',1,100)
st.text(n)
plt.subplot(2,1,1)
plt.plot(x,(psi(x,n)),label=rf'$\psi_{n}$')
plt.xlim(0,a)
plt.axhline(0,color='black')
plt.subplot(2,1,2)
plt.plot(x,(psi(x,n))**2,label=rf'$\psi_{n}$')
plt.ylabel('$\psi(x)^2$')
plt.xlabel('x')
plt.xlim(0,a)
plt.ylim(bottom=0)
plt.savefig('graph.jpg')
st.image('graph.jpg')

def psi1(x, n):
    y = np.sqrt(1 / (a)) * np.sin((n * np.pi * x) / (a))
    return y

plt.subplot(2,1,1)
plt.plot(x,(psi(x,n)),label=rf'$\psi_{n}$')
plt.xlim(-a,a)
plt.axhline(0,color='black')
plt.axhline(0,color='black')
plt.axvline(0,color='black')
plt.subplot(2,1,2)
plt.plot(x,(psi(x,n))**2,label=rf'$\psi_{n}$')
plt.ylabel('$\psi(x)^2$')
plt.xlabel('x')
plt.xlim(-a,a)
plt.axvline(0,color='black')
plt.ylim(bottom=0)
plt.savefig('graph1.jpg')
st.image('graph1.jpg')

options = st.multiselect('Choose the type of well',['Asymmetric Potential Well','Symmetric Potential Well'])
