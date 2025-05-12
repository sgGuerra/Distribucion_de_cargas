import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def campo_electrico_neto(Q, a):
    # Constante electrostática k = 1/(4πε₀) donde ε₀ es la permitividad del vacío
    epsilon_0 = 8.85e-12  # Permitividad del vacío en F/m
    k = 1 / (4 * np.pi * epsilon_0)  # Constante de Coulomb en N⋅m²/C²
    
    # Densidad lineal de carga (C/m)
    lambda_pos = Q / (np.pi * a / 2)  # Para la mitad izquierda
    lambda_neg = -Q / (np.pi * a / 2)  # Para la mitad derecha
    
    # Función integrando para la componente x del campo eléctrico
    def integrando_x(theta):
        return np.cos(theta)   
    
    # Integrar de 0 a pi/2 y multiplicar por 2 (por simetría)
    resultado_pos = (2 * k * lambda_pos)/ (a**2) * quad(integrando_x, 0, np.pi/2)[0]
    resultado_neg = (2 * k * lambda_neg)/ (a**2) * quad(integrando_x, np.pi/2, np.pi)[0]
    
    # El campo eléctrico neto es la suma de ambas contribuciones
    E_neto = resultado_pos + resultado_neg
    
    return abs(E_neto)

def graficar_distribucion(a, fig, mostrar_leyenda=True):
    """
    Grafica la distribución de carga en el semicírculo
    
    Parámetros:
    a : float
        Radio en metros
    fig : Figure
        Figura de matplotlib donde graficar
    mostrar_leyenda : bool
        Si se debe mostrar la leyenda
    """
    fig.clear()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0.15, right=0.85, bottom=0.15, top=0.92)
    
    theta = np.linspace(0, np.pi, 100)
    x = a * np.cos(theta)  # Radio en metros
    y = a * np.sin(theta)  # Radio en metros
    
    # Graficar el semicírculo
    ax.plot(x[x <= 0], y[x <= 0], 'r-', linewidth=2, label='Carga positiva (+Q)')
    ax.plot(x[x >= 0], y[x >= 0], 'b-', linewidth=2, label='Carga negativa (-Q)')
    ax.plot(0, 0, 'ko', markersize=8, label='Origen')
    
    # Dibuja una flecha para mostrar la dirección del campo eléctrico
    ax.arrow(0, 0, a/2, 0, 
             head_width=a/20, head_length=a/10,
             fc='g', ec='g', linewidth=2, label='Campo Eléctrico')
    
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_xlabel('x (m)', fontsize=10)
    ax.set_ylabel('y (m)', fontsize=10)
    ax.set_title('Distribución de carga en semicírculo', pad=10)
    
    # Establecer límites y escala
    xlim = a * 1.5
    ylim = a * 1.2
    ax.set_xlim(-xlim, xlim)
    ax.set_ylim(-a*0.1, ylim)
    
    # Ajustar número de ticks según el tamaño
    num_ticks = 7 if a >= 1 else 5
    xticks = np.linspace(-a, a, num_ticks)
    yticks = np.linspace(0, a, num_ticks-2)
    
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    
    # Formatear los números según el tamaño
    if a >= 10:
        formato = '%.1f'
    elif a >= 1:
        formato = '%.2f'
    else:
        formato = '%.3f'
    
    ax.xaxis.set_major_formatter(plt.FormatStrFormatter(formato))
    ax.yaxis.set_major_formatter(plt.FormatStrFormatter(formato))
    
    if mostrar_leyenda:
        legend = ax.legend(loc='upper right', bbox_to_anchor=(0.98, 0.98),
                          fontsize=9, framealpha=0.9)
        legend.get_frame().set_linewidth(0.5)
    
    ax.set_aspect('equal')

class AplicacionCampoElectrico:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Campo Eléctrico")
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Entradas
        ttk.Label(main_frame, text="Carga Q (µC):").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.q_var = tk.StringVar(value="1.0")
        ttk.Entry(main_frame, textvariable=self.q_var, width=15).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Radio a (m):").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.a_var = tk.StringVar(value="0.1")
        ttk.Entry(main_frame, textvariable=self.a_var, width=15).grid(row=1, column=1, padx=5, pady=5)
        
        # Frame para botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Calcular", command=self.calcular).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Reiniciar", command=self.reiniciar).grid(row=0, column=1, padx=5)
        
        # Frame para resultados
        self.results_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        self.results_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.resultado_var = tk.StringVar()
        ttk.Label(self.results_frame, textvariable=self.resultado_var, wraplength=400).grid(row=0, column=0)
        
        # Configurar el área de la gráfica
        self.fig = Figure(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=main_frame)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        
        # Inicializar gráfica vacía
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xlabel('x (m)', fontsize=10)
        ax.set_ylabel('y (m)', fontsize=10)
        ax.set_title('Distribución de carga en semicírculo', pad=10)
        ax.set_xlim(-0.15, 0.15)  # Valores predeterminados en metros
        ax.set_ylim(-0.015, 0.12)
        ax.set_aspect('equal')
        self.canvas.draw()
    
    def reiniciar(self):
        """Restablece los valores por defecto y limpia la gráfica"""
        # Restablecer valores de entrada
        self.q_var.set("1.0")
        self.a_var.set("0.1")
        self.resultado_var.set("")
        
        # Limpiar y reiniciar la gráfica
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.set_xlabel('x (m)', fontsize=10)
        ax.set_ylabel('y (m)', fontsize=10)
        ax.set_title('Distribución de carga en semicírculo', pad=10)
        ax.set_xlim(-0.15, 0.15)  # Valores predeterminados en metros
        ax.set_ylim(-0.015, 0.12)
        ax.set_aspect('equal')
        self.canvas.draw()
    
    def calcular(self):
        """Calcula y muestra el campo eléctrico"""
        try:
            Q = float(self.q_var.get()) * 1e-6  # Convertir µC a C
            a = float(self.a_var.get())  # Radio en metros
            
            if a <= 0:
                raise ValueError("El radio debe ser mayor que cero")
            
            E = campo_electrico_neto(Q, a)
            
            # Actualizar texto de resultados
            resultado_texto = (
                f"Carga ingresada: {Q*1e6:.1f} µC\n"
                f"Radio ingresado: {a:.3f} m\n"
                f"Campo eléctrico neto: {E/1000:.2f} kN/C\n"
                f"Dirección: A lo largo del eje x positivo"
            )
            self.resultado_var.set(resultado_texto)
            
            # Actualizar gráfica
            graficar_distribucion(a, self.fig)
            self.canvas.draw()
            
        except ValueError as e:
            if str(e) == "El radio debe ser mayor que cero":
                self.resultado_var.set("Error: El radio debe ser mayor que cero")
            else:
                self.resultado_var.set("Error: Por favor ingrese valores numéricos válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionCampoElectrico(root)
    root.mainloop()