# prompt: imprimir dataframe usando streamlit
import plotly.express as px
import streamlit as st
import pandas as pd

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.dataframe(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
  st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  
  # Verifica si la columna 'Region' existe en el DataFrame
  if 'Region' in df.columns:
    # Crea la gráfica de ventas por región
    fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región') # Reemplaza 'Ventas' con el nombre de tu columna de ventas
    st.plotly_chart(fig)
  else:
      st.error("La columna 'Region' no se encuentra en el archivo.")
  
  st.dataframe(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
  st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")

    # prompt: usando el dataframe df, crear un filtro con la columna region y otro con la columna state donde el resultado sea en una misma tabla

# Assuming 'df' is your DataFrame and it has columns named 'Region' and 'State'

region_filter = st.multiselect("Select Region", df['Region'].unique())
state_filter = st.multiselect("Select State", df['State'].unique())


if region_filter and state_filter :
  filtered_df = df[(df['Region'].isin(region_filter)) & (df['State'].isin(state_filter))]
elif region_filter:
  filtered_df = df[df['Region'].isin(region_filter)]
elif state_filter:
  filtered_df = df[df['State'].isin(state_filter)]
else:
  filtered_df = df # No filter applied


st.dataframe(filtered_df)

# Create the pie chart based on the 'State' column
if 'State' in filtered_df.columns:
    fig_pie = px.pie(filtered_df, names='State', title='Distribution by State')
    st.plotly_chart(fig_pie)
else:
    st.error("The 'State' column is not found in the DataFrame.")
import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinal.xlsx')
    print(df.head())  # Muestra las primeras filas del DataFrame
    print(df.columns)  # Imprime los nombres de las columnas del DataFrame
except FileNotFoundError:
    print("Error: El archivo 'SalidaFinal.xlsx' no se encuentra.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")

# Asegúrate de que la columna 'Order Date' esté en formato de fecha
df['Order Date'] = pd.to_datetime(df['Order Date'])
# Agrupa por región y suma las ventas
try:
   
    sales_by_region = df.groupby('Region')['Sales'].sum()

    # Crea la gráfica de barras con Plotly Express
    fig = px.bar(sales_by_region, 
                 x=sales_by_region.index, 
                 y='Sales', 
                 title='Ventas Acumuladas por Región',
                 labels={'Sales': 'Ventas', 'x': 'Región'})
    
    st.plotly_chart(fig)

    # Agrupa por año y categoría, y suma las ventas
    df['Year'] = df['Order Date'].dt.year
    sales_by_year_category = df.groupby(['Year', 'Category'])['Sales'].sum().reset_index()

    # Crea la gráfica de línea con Plotly Express
    fig_line = px.line(sales_by_year_category, 
                       x='Year', 
                       y='Sales', 
                       color='Category',
                       title='Ventas Acumuladas por Año y Categoría',
                       labels={'Sales': 'Ventas', 'Year': 'Año', 'Category': 'Categoría'})
    
    st.plotly_chart(fig_line)

     # Crea la gráfica de barras apiladas con Plotly Express
    fig_bar = px.bar(sales_by_year_category, 
                     x='Year', 
                     y='Sales', 
                     color='Category',
                     title='Ventas Acumuladas por Año y Categoría (Barras)',
                     labels={'Sales': 'Ventas', 'Year': 'Año', 'Category': 'Categoría'},
                     barmode='stack')
    
    st.plotly_chart(fig_bar)

    sales_by_year_category_subcategory = df.groupby(['Year', 'Category', 'Sub-Category'])['Sales'].sum().reset_index()

   

   # Crea la gráfica de barras apiladas por categoría y subcategoría
    fig_bar_category = px.bar(sales_by_year_category_subcategory, 
                              x='Year', 
                              y='Sales', 
                              color='Sub-Category',
                              title='Ventas Acumuladas por Año, Categoría y Sub-Categoría (Barras)',
                              labels={'Sales': 'Ventas', 'Year': 'Año', 'Category': 'Categoría', 'Sub-Category': 'Sub-Categoría'},
                              barmode='stack',
                              facet_col='Category')
    st.plotly_chart(fig_bar_category)

    # Crea la gráfica de barras apiladas por categoría y subcategoría
    fig_bar_category = px.bar(sales_by_year_category_subcategory, 
                              x='Category', 
                              y='Sales', 
                              color='Sub-Category',
                              title='Ventas Acumuladas por Año, Categoría y Sub-Categoría (Barras)',
                              labels={'Sales': 'Ventas', 'Year': 'Año', 'Category': 'Categoría', 'Sub-Category': 'Sub-Categoría'},
                              barmode='stack',
                              facet_col='Year')
    st.plotly_chart(fig_bar_category)
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinal.xlsx' no se encuentra.")
except Exception as e:
    st.error(f"Error al leer el archivo o generar la gráfica: {e}")
