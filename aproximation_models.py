import numpy as np
import pandas as pd
import scipy.optimize


class ApproximationModels:
    @staticmethod
    def linear(x, b_0, b_1):
        return b_0 + b_1 * x

    @staticmethod
    def quadratic(x, b_0, b_1, b_2):
        return b_0 + b_1 * x + b_2 * (x**2)

    @staticmethod
    def cubic(x, b_0, b_1, b_2, b_3):
        return b_0 + b_1 * x + b_2 * (x**2) + b_3 * (x**3)

    @staticmethod
    def polynomial_4(x, b0, b1, b2, b3, b4):
        return b4 * x**4 + b3 * x**3 + b2 * x**2 + b1 * x + b0

    @staticmethod
    def power(X, b0, b1):
        """Степенная: Y = b0 * X^b1"""
        return b0 * X**b1

    @staticmethod
    def exponential_type_1(X, b0, b1):
        """Экспоненциальная I типа: Y = b0 * e^(b1 * X)"""
        return b0 * np.exp(b1 * X)

    @staticmethod
    def exponential_type_2(X, b0, b1):
        """Экспоненциальная II типа: Y = b0 * b1^X"""
        return b0 * b1**X

    @staticmethod
    def logarithmic(X, b0, b1):
        """Логарифмическая: Y = b0 + b1 * ln(X)"""
        return b0 + b1 * np.log(X)

    @staticmethod
    def inverse_logarithmic(X, b0, b1):
        """Обратная логарифмическая: Y = 1 / (b0 + b1 * ln(X))"""
        return 1 / (b0 + b1 * np.log(X))

    @staticmethod
    def hyperbolic_type_1(X, b0, b1):
        """Гиперболическая I типа: Y = b0 + b1 / X"""
        return b0 + b1 / X

    @staticmethod
    def hyperbolic_type_2(X, b0, b1):
        """Гиперболическая II типа: Y = 1 / (b0 + b1 * X)"""
        return 1 / (b0 + b1 * X)

    @staticmethod
    def hyperbolic_type_3(X, b0, b1):
        """Гиперболическая III типа: Y = X / (b0 + b1 * X)"""
        return X / (b0 + b1 * X)

    @staticmethod
    def logistic_curve_type_1(X, b0, b1, b2):
        """Логистическая кривая I типа: Y = b0 / (1 + b1 * e^(-b2 * X))"""
        return b0 / (1 + b1 * np.exp(-b2 * X))

    @staticmethod
    def logistic_curve_type_2(X, b0, b1, b2):
        """Логистическая кривая II типа (Перла-Рида): Y = b0 / (1 + b1 * b2^(-X))"""
        return b0 / (1 + b1 * b2 ** (-X))

    @staticmethod
    def gompertz_curve(X, b0, b1, b2):
        """Кривая Гомперца: Y = b0 * b1^(b2^X)"""
        return b0 * b1 ** (b2**X)

    @staticmethod
    def modified_exponential_type_1(X, b0, b1, b2):
        """Модифицированная экспонента I типа: Y = b0 + b1 * e^(b2 * X)"""
        return b0 + b1 * np.exp(b2 * X)

    @staticmethod
    def modified_exponential_type_2(X, b0, b1, b2):
        """Модифицированная экспонента II типа: Y = b0 + b1 * b2^X"""
        return b0 + b1 * b2**X

    @staticmethod
    def generalized_logistic_curve_type_1(X, b0, b1, b2, b3):
        """Обобщенная логистическая кривая I типа: Y = b0 + b1 / (1 + b2 * e^(-b3 * X))"""
        return b0 + b1 / (1 + b2 * np.exp(-b3 * X))

    @staticmethod
    def generalized_logistic_curve_type_2(X, b0, b1, b2, b3):
        """Обобщенная логистическая кривая II типа: Y = b0 + b1 / (1 + b2 * b3^(-X))"""
        return b0 + b1 / (1 + b2 * b3 ** (-X))


if __name__ == "__main__":

    df = pd.read_csv("exp_8.csv")
    base_x = df["cycles"]
    base_y = df["top_mean_values"]

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.linear, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"Linear: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.quadratic, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"Quadratic: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.cubic, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"Cubic: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.polynomial_4, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"Polynomial_4: {perr}")

    _, pcov = scipy.optimize.curve_fit(ApproximationModels.power, base_x, base_y)
    perr = np.sqrt(np.diag(pcov))
    print(f"Power: {perr}")

    _, pcov = scipy.optimize.curve_fit(ApproximationModels.exponential_type_1, base_x, base_y)
    perr = np.sqrt(np.diag(pcov))
    print(f"exponential_type_1: {perr}")

    _, pcov = scipy.optimize.curve_fit(ApproximationModels.exponential_type_2, base_x, base_y)
    perr = np.sqrt(np.diag(pcov))
    print(f"exponential_type_2: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.logarithmic, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"logarithmic: {perr}")

    _, pcov = scipy.optimize.curve_fit(ApproximationModels.inverse_logarithmic, base_x, base_y)
    perr = np.sqrt(np.diag(pcov))
    print(f"inverse_logarithmic: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.hyperbolic_type_1, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"hyperbolic_type_1: {perr}")

    _, pcov = scipy.optimize.curve_fit(ApproximationModels.hyperbolic_type_2, base_x, base_y)
    perr = np.sqrt(np.diag(pcov))
    print(f"hyperbolic_type_2: {perr}")

    _, pcov = scipy.optimize.curve_fit(ApproximationModels.hyperbolic_type_3, base_x, base_y)
    perr = np.sqrt(np.diag(pcov))
    print(f"hyperbolic_type_3: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.logistic_curve_type_1, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"logistic_curve_type_1: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.logistic_curve_type_2, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"logistic_curve_type_2: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.gompertz_curve, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"gompertz_curve: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.modified_exponential_type_1, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"modified_exponential_type_1: {perr}")
    #
    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.modified_exponential_type_2, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"modified_exponential_type_2: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.generalized_logistic_curve_type_1, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"generalized_logistic_curve_type_1: {perr}")

    # _, pcov = scipy.optimize.curve_fit(ApproximationModels.generalized_logistic_curve_type_2, base_x, base_y)
    # perr = np.sqrt(np.diag(pcov))
    # print(f"generalized_logistic_curve_type_2: {perr}")
