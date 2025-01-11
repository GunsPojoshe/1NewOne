
import plotly.express as px

class VisualizationService:
    def __init__(self, data: dict):
        """
        Инициализация сервиса визуализации.
        
        :param data: Данные для визуализации.
        """
        self.data = data

    def plot_sales(self) -> str:
        """
        Построить график продаж.
        
        :return: HTML-код графика.
        """
        df = pd.DataFrame(self.data)
        fig = px.bar(df, x="product_name", y="price", title="Продажи по товарам")
        return fig.to_html()