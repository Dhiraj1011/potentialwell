
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
plt.plot(x,(psi(x,n)))
plt.axhline(0)
plt.subplot(2,1,2)
plt.plot(x,(psi(x,n))**2,'--',label=rf'$\psi_{n}$')
plt.ylabel('$\psi(x)^2$')
plt.xlabel('x')
plt.xlim(0,a)
plt.ylim(bottom=0)
plt.savefig('graph.jpg')
st.image('graph.jpg')

