"""
Tests para el mÃ³dulo encftr de endompy.
"""

import pytest
import pandas as pd
from endompy import EncftDataFrame


class TestEncftDataFrame:
    """Tests para la clase EncftDataFrame."""

    def test_creation_from_dict(self):
        """Verifica que se puede crear un EncftDataFrame desde un diccionario."""
        data = {"FACTOR_EXPANSION": [1028, 848, 400], "otra_columna": [1, 2, 3]}
        df = EncftDataFrame(data)

        assert isinstance(df, EncftDataFrame)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 3
        assert "FACTOR_EXPANSION" in df.columns

    def test_creation_from_dataframe(self):
        """Verifica que se puede crear un EncftDataFrame desde un DataFrame."""
        pdf = pd.DataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        df = EncftDataFrame(pdf)

        assert isinstance(df, EncftDataFrame)
        assert len(df) == 3


class TestFactorExpansionAnual:
    """Tests para el mÃ©todo factor_expansion_anual."""

    def test_calculation_is_correct(self):
        """Verifica que el cÃ¡lculo FACTOR_EXPANSION / 4 es correcto."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        result = df.factor_expansion_anual(periods=4)

        expected = [257.0, 212.0, 100.0]
        assert result["factor_expansion_anual"].tolist() == expected

    def test_returns_encft_dataframe(self):
        """Verifica que el resultado es un EncftDataFrame."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        result = df.factor_expansion_anual(periods=4)

        assert isinstance(result, EncftDataFrame)

    def test_original_unchanged(self):
        """Verifica que el DataFrame original no se modifica."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        _ = df.factor_expansion_anual(periods=4)

        assert "factor_expansion_anual" not in df.columns

    def test_missing_column_raises_error(self):
        """Verifica que se lanza error si falta FACTOR_EXPANSION."""
        df = EncftDataFrame({"otra_columna": [1, 2, 3]})

        with pytest.raises(ValueError) as excinfo:
            df.factor_expansion_anual(periods=4)

        assert "FACTOR_EXPANSION" in str(excinfo.value)


class TestFactorExpansionSemestre:
    """Tests para el mÃ©todo factor_expansion_semestre."""

    def test_calculation_is_correct(self):
        """Verifica que el cÃ¡lculo FACTOR_EXPANSION / 2 es correcto."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        result = df.factor_expansion_semestre(periods=2)

        expected = [514.0, 424.0, 200.0]
        assert result["factor_expansion_semestre"].tolist() == expected

    def test_returns_encft_dataframe(self):
        """Verifica que el resultado es un EncftDataFrame."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        result = df.factor_expansion_semestre(periods=2)

        assert isinstance(result, EncftDataFrame)


class TestDataFrameOperations:
    """Tests para verificar que operaciones de pandas funcionan correctamente."""

    def test_slicing_works(self):
        """Verifica que slicing funciona correctamente."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400], "x": [1, 2, 3]})
        sliced = df[df["x"] > 1]

        assert isinstance(sliced, EncftDataFrame)
        assert len(sliced) == 2

    def test_copy_preserves_type(self):
        """Verifica que copy() preserva el tipo EncftDataFrame."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        copied = df.copy()

        assert isinstance(copied, EncftDataFrame)

    def test_chaining_methods(self):
        """Verifica que se pueden encadenar mÃ©todos."""
        df = EncftDataFrame({"FACTOR_EXPANSION": [1028, 848, 400]})
        result = df.factor_expansion_anual(periods=4).factor_expansion_semestre(periods=2)

        assert "factor_expansion_anual" in result.columns
        assert "factor_expansion_semestre" in result.columns
