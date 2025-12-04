"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    def cargar_datos(ruta):
        return pd.read_csv(ruta, index_col=0)

    def aplicar_estilo_grafico():
        plt.title("How people get their news", fontsize=16)
        ax = plt.gca()
        ax.spines["top"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.yaxis.set_visible(False)

    def anotar_extremos(df, colores, zorders):
        for medio in df.columns:
            anio_inicial = df.index[0]
            anio_final = df.index[-1]
            valor_ini = df.loc[anio_inicial, medio]
            valor_fin = df.loc[anio_final, medio]
            plt.scatter(anio_inicial, valor_ini, color=colores[medio], zorder=zorders[medio])
            plt.text(
                anio_inicial - 0.2,
                valor_ini,
                f"{medio} {valor_ini}%",
                ha="right",
                va="center",
                color=colores[medio],
            )
            plt.scatter(anio_final, valor_fin, color=colores[medio], zorder=zorders[medio])
            plt.text(
                anio_final + 0.2,
                valor_fin,
                f"{valor_fin}%",
                ha="left",
                va="center",
                color=colores[medio],
            )


    plt.figure()
    datos = cargar_datos("files/input/news.csv")
    colores = {
    "Television": "dimgray",
    "Newspaper": "grey",
    "Internet": "tab:blue",
    "Radio": "lightgrey",
    }
    zorders = {"Television": 1, "Newspaper": 1, "Internet": 2, "Radio": 1}
    linewidths = {"Television": 2, "Newspaper": 2, "Internet": 4, "Radio": 2}
    for medio in datos.columns:
        plt.plot(
            datos[medio],
            color=colores[medio],
            label=medio,
            zorder=zorders[medio],
            linewidth=linewidths[medio],
        )
    aplicar_estilo_grafico()
    anotar_extremos(datos, colores, zorders)
    plt.xticks(ticks=datos.index, labels=datos.index, ha="center")
    os.makedirs("files/plots", exist_ok=True)
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()
