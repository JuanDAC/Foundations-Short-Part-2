from abc import ABCMeta, abstractmethod
from typing import Callable, Optional, Optional, TypeVar, Tuple
from abc import ABCMeta, abstractproperty, abstractmethod
import unittest

T = TypeVar('T')

# Interfaz para obtener el valor de un nodo en el árbol binario
class ValorObtenible(metaclass=ABCMeta):
    @abstractproperty
    def valor(self) -> T:
        """
        Propiedad abstracta para obtener el valor almacenado en el nodo.

        Returns:
            int: El valor almacenado en el nodo.
        """
        pass


# Interfaz para obtener el valor de un nodo en el árbol binario
class PadreObtenible(metaclass=ABCMeta):
    @abstractproperty
    def padre(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al padre del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al padre del nodo actual.
        """
        pass


# Interfaz para obtener los hijos izquierdo y derecho de un nodo en el árbol binario
class HijosObtenibles(metaclass=ABCMeta):
    @abstractproperty
    def izquierda(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al hijo izquierdo del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo izquierdo del nodo actual.
        """
        pass

    @izquierda.setter
    @abstractmethod
    def izquierda(self, value: 'NodoInterface') -> None:
        """
        Propiedad abstracta para establecer el nodo que representa al hijo izquierdo del nodo actual.

        Args:
            value (NodoInterface): El nodo que representa al hijo izquierdo del nodo actual.
        """
        pass

    @abstractproperty
    def derecha(self) -> 'NodoInterface':
        """
        Propiedad abstracta para obtener el nodo que representa al hijo derecho del nodo actual.

        Returns:
            NodoInterface: El nodo que representa al hijo derecho del nodo actual.
        """
        pass

    @derecha.setter
    @abstractmethod
    def derecha(self, value: 'NodoInterface') -> None:
        """
        Propiedad abstracta para establecer el nodo que representa al hijo derecho del nodo actual.

        Args:
            value (NodoInterface): El nodo que representa al hijo derecho del nodo actual.
        """
        pass

# Interfaz completa para un nodo en el árbol binario
class NodoInterface(ValorObtenible, HijosObtenibles, PadreObtenible, metaclass=ABCMeta):
    """
    Interfaz que define los métodos que debe implementar cualquier clase que actúe como un nodo en un árbol binario.
    La interfaz incluye métodos para obtener el valor del nodo y sus hijos izquierdo y derecho.
    """
    pass


class Nodo(NodoInterface):
    # Tu nodo aqui
    pass

# Interfaz para operaciones de inserción en el árbol
class OperacionesInsercion(metaclass=ABCMeta):
    @abstractmethod
    def insertar(self, valor: T, proposicion: Callable[[T, T], bool]) -> None:
        pass

    @abstractmethod
    def insertarAll(self, valores: Tuple[T], proposicion: Callable[[T, T], bool]) -> None:
        pass

# Interfaz para operaciones de búsqueda en el árbol
class OperacionesBusqueda(metaclass=ABCMeta):

    @abstractmethod
    def buscar(self, valor: T) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def buscarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def buscarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz para operaciones de eliminación eßßßn el árbol
class OperacionesEliminacion(metaclass=ABCMeta):
    @abstractmethod
    def eliminar(self, valor: T) -> None:
        pass

    @abstractmethod
    def eliminarAll(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def eliminarWhere(self, proposicion: Callable[[Optional[NodoInterface]], bool]) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz para operaciones de consulta en el árbol
class OperacionesConsulta(metaclass=ABCMeta):
    @abstractmethod
    def obtener_minimo(self, proposicion: Callable[[Optional[NodoInterface]], int]) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def obtener_maximo(self, proposicion: Callable[[Optional[NodoInterface]], int]) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def altura(self) -> int:
        pass

    @abstractmethod
    def es_hoja(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def esta_derecho(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def esta_izquierdo(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def es_raiz(self, nodo: Optional[NodoInterface]) -> bool:
        pass

    @abstractmethod
    def es_vacio(self) -> bool:
        pass

    @abstractmethod
    def cantidad_nodos(self) -> int:
        pass

    @abstractmethod
    def recorrido_inorder(self) -> Tuple[T]:
        pass

    @abstractmethod
    def recorrido_preorder(self) -> Tuple[T]:
        pass

    @abstractmethod
    def recorrido_postorder(self) -> Tuple[T]:
        pass

    @abstractproperty
    def root(self) -> Optional[NodoInterface]:
        pass

# Interfaz para operaciones de árbol binario de búsqueda
class ArbolBinarioBusqueda(metaclass=ABCMeta):
    @abstractmethod
    def es_arbol_binario_busqueda(self) -> bool:
        pass

    @abstractmethod
    def obtener_padre(self, valor: T) -> Optional[NodoInterface]:
        pass

    @abstractmethod
    def obtener_hermanos(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def nivel_nodo(self, valor: T) -> int:
        pass

    @abstractmethod
    def ancestros(self, valor: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def cantidad_hojas(self) -> int:
        pass

# Interfaz para operaciones de árbol con propiedades específicas
class ArbolConPropiedades(metaclass=ABCMeta):
    @abstractmethod
    def es_simetrico(self) -> bool:
        pass

    @abstractmethod
    def es_completo(self) -> bool:
        pass

    @abstractmethod
    def es_balanceado(self) -> bool:
        pass

    @abstractmethod
    def recorrido_por_nivel(self) -> Tuple[Tuple[T]]:
        pass

    @abstractmethod
    def obtener_ancestros_comunes(self, valor1: T, valor2: T) -> Tuple[Optional[NodoInterface]]:
        pass

    @abstractmethod
    def camino_entre_nodos(self, valor1: T, valor2: T) -> Tuple[Optional[NodoInterface]]:
        pass

# Interfaz que combina todas las operaciones de un árbol binario
class Arbol(OperacionesInsercion, OperacionesBusqueda, OperacionesEliminacion, OperacionesConsulta, ArbolBinarioBusqueda, ArbolConPropiedades, metaclass=ABCMeta):
    pass


class ArbolBinario(Arbol):
    # Tu codigo aqui
    pass

class TestArbolConPropiedades(unittest.TestCase):
    def setUp(self):
        # Crear un árbol de ejemplo para realizar pruebas
        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo6 = Nodo(12)
        nodo7 = Nodo(18)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        nodo3.izquierda = nodo6
        nodo3.derecha = nodo7
        self.arbol = ArbolBinario(nodo1)

    def test_es_simetrico(self):
        self.assertFalse(self.arbol.es_simetrico())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(5)
        nodo4 = Nodo(3)
        nodo5 = Nodo(3)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo3.derecha = nodo5
        arbol_simetrico = ArbolBinario(nodo1)
        self.assertTrue(arbol_simetrico.es_simetrico())

    def test_es_completo(self):
        self.assertFalse(self.arbol.es_completo())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo6 = Nodo(12)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        nodo3.izquierda = nodo6
        arbol_completo = ArbolBinario(nodo1)
        self.assertTrue(arbol_completo.es_completo())

    def test_es_balanceado(self):
        self.assertFalse(self.arbol.es_balanceado())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo3.derecha = nodo5
        arbol_balanceado = ArbolBinario(nodo1)
        self.assertTrue(arbol_balanceado.es_balanceado())

    def test_recorrido_por_nivel(self):
        resultado = self.arbol.recorrido_por_nivel()
        expected = ((10,), (5, 15), (3, 7, 12, 18))
        self.assertEqual(resultado, expected)

    def test_obtener_ancestros_comunes(self):
        resultado = self.arbol.obtener_ancestros_comunes(3, 7)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 5)

        resultado = self.arbol.obtener_ancestros_comunes(12, 18)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 15)

        resultado = self.arbol.obtener_ancestros_comunes(3, 18)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 10)

    def test_camino_entre_nodos(self):
        resultado = self.arbol.camino_entre_nodos(3, 7)
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0].valor, 3)
        self.assertEqual(resultado[1].valor, 5)
        self.assertEqual(resultado[2].valor, 7)

        resultado = self.arbol.camino_entre_nodos(12, 18)
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0].valor, 12)
        self.assertEqual(resultado[1].valor, 15)
        self.assertEqual(resultado[2].valor, 18)


class TestArbolBinarioBusqueda(unittest.TestCase):
    def setUp(self):
        # Crear un árbol de búsqueda binaria para realizar pruebas
        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo6 = Nodo(12)
        nodo7 = Nodo(18)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        nodo3.izquierda = nodo6
        nodo3.derecha = nodo7
        self.arbol = ArbolBinario(nodo1)

    def test_es_arbol_binario_busqueda(self):
        self.assertTrue(self.arbol.es_arbol_binario_busqueda())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo1.izquierda = nodo3
        nodo1.derecha = nodo2
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        arbol_no_busqueda = ArbolBinario(nodo1)
        self.assertFalse(arbol_no_busqueda.es_arbol_binario_busqueda())

    def test_obtener_padre(self):
        resultado = self.arbol.obtener_padre(3)
        self.assertEqual(resultado.valor, 5)

        resultado = self.arbol.obtener_padre(15)
        self.assertEqual(resultado.valor, 10)

        resultado = self.arbol.obtener_padre(10)
        self.assertIsNone(resultado)

    def test_obtener_hermanos(self):
        resultado = self.arbol.obtener_hermanos(3)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 7)

        resultado = self.arbol.obtener_hermanos(15)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 5)

        resultado = self.arbol.obtener_hermanos(10)
        self.assertEqual(len(resultado), 0)

    def test_nivel_nodo(self):
        resultado = self.arbol.nivel_nodo(3)
        self.assertEqual(resultado, 2)

        resultado = self.arbol.nivel_nodo(15)
        self.assertEqual(resultado, 2)

        resultado = self.arbol.nivel_nodo(10)
        self.assertEqual(resultado, 1)

    def test_ancestros(self):
        resultado = self.arbol.ancestros(3)
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0].valor, 5)
        self.assertEqual(resultado[1].valor, 10)

        resultado = self.arbol.ancestros(15)
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0].valor, 12)
        self.assertEqual(resultado[1].valor, 10)

        resultado = self.arbol.ancestros(10)
        self.assertEqual(len(resultado), 0)

    def test_cantidad_hojas(self):
        cantidad = self.arbol.cantidad_hojas()
        self.assertEqual(cantidad, 4)

class TestArbolConPropiedades(unittest.TestCase):
    def setUp(self):
        # Crear un árbol de ejemplo para realizar pruebas
        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo6 = Nodo(12)
        nodo7 = Nodo(18)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        nodo3.izquierda = nodo6
        nodo3.derecha = nodo7
        self.arbol = ArbolBinario(nodo1)

    def test_es_simetrico(self):
        self.assertFalse(self.arbol.es_simetrico())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(5)
        nodo4 = Nodo(3)
        nodo5 = Nodo(3)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo3.derecha = nodo5
        arbol_simetrico = ArbolBinario(nodo1)
        self.assertTrue(arbol_simetrico.es_simetrico())

    def test_es_completo(self):
        self.assertFalse(self.arbol.es_completo())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo6 = Nodo(12)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        nodo3.izquierda = nodo6
        arbol_completo = ArbolBinario(nodo1)
        self.assertTrue(arbol_completo.es_completo())

    def test_es_balanceado(self):
        self.assertFalse(self.arbol.es_balanceado())

        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo3.derecha = nodo5
        arbol_balanceado = ArbolBinario(nodo1)
        self.assertTrue(arbol_balanceado.es_balanceado())

    def test_recorrido_por_nivel(self):
        resultado = self.arbol.recorrido_por_nivel()
        expected = ((10,), (5, 15), (3, 7, 12, 18))
        self.assertEqual(resultado, expected)

    def test_obtener_ancestros_comunes(self):
        resultado = self.arbol.obtener_ancestros_comunes(3, 7)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 5)

        resultado = self.arbol.obtener_ancestros_comunes(12, 18)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 15)

        resultado = self.arbol.obtener_ancestros_comunes(3, 18)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].valor, 10)

    def test_camino_entre_nodos(self):
        resultado = self.arbol.camino_entre_nodos(3, 7)
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0].valor, 3)
        self.assertEqual(resultado[1].valor, 5)
        self.assertEqual(resultado[2].valor, 7)

        resultado = self.arbol.camino_entre_nodos(12, 18)
        self.assertEqual(len(resultado), 3)
        self.assertEqual(resultado[0].valor, 12)
        self.assertEqual(resultado[1].valor, 15)
        self.assertEqual(resultado[2].valor, 18)


# Clase de prueba para ArbolBinario
class TestArbol(unittest.TestCase):
    def test_asignar_raiz(self):
        nodo = Nodo(10)
        arbol = ArbolBinario(nodo)
        self.assertEqual(arbol._ArbolBinario__raiz, nodo)

    def test_raiz_vacia(self):
        arbol = ArbolBinario()
        self.assertIsNone(arbol._ArbolBinario__raiz)

    def test_insertar_raiz(self):
        arbol = ArbolBinario(Nodo(10))
        self.assertEqual(arbol._ArbolBinario__raiz.valor, 10)
        
    def test_insertar_izquierda(self):
        arbol = ArbolBinario(Nodo(10))
        arbol.insertar(5, lambda x, y: x < y)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.valor, 5)

    def test_insertar_derecha(self):
        arbol = ArbolBinario(Nodo(10))
        arbol.insertar(15, lambda x, y: x < y)
        self.assertEqual(arbol._ArbolBinario__raiz.derecha.valor, 15)

    def test_insertarAll(self):
        arbol = ArbolBinario(Nodo(10))
        arbol.insertarAll((5, 15, 3, 7), lambda x, y: x < y)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.valor, 5)
        self.assertEqual(arbol._ArbolBinario__raiz.derecha.valor, 15)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.izquierda.valor, 3)
        self.assertEqual(arbol._ArbolBinario__raiz.izquierda.derecha.valor, 7)

    def setUp(self):
        nodo1 = Nodo(10)
        nodo2 = Nodo(5)
        nodo3 = Nodo(15)
        nodo4 = Nodo(3)
        nodo5 = Nodo(7)
        nodo1.izquierda = nodo2
        nodo1.derecha = nodo3
        nodo2.izquierda = nodo4
        nodo2.derecha = nodo5
        self.arbol = ArbolBinario(nodo1)

    def test_buscar_existente(self):
        resultado = self.arbol.buscar(10)
        self.assertEqual(resultado.valor, 10)

    def test_buscar_no_existente(self):
        resultado = self.arbol.buscar(20)
        self.assertIsNone(resultado)

    def test_buscarAll_existente(self):
        resultados = self.arbol.buscarAll(5)
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].valor, 5)

    def test_buscarAll_no_existente(self):
        resultados = self.arbol.buscarAll(20)
        self.assertEqual(len(resultados), 0)

    def test_buscarWhere_proposicion(self):
        def es_menor_que_10(nodo: Optional[NodoInterface]) -> bool:
            return nodo is not None and nodo.valor < 10

        resultados = self.arbol.buscarWhere(es_menor_que_10)
        self.assertEqual(len(resultados), 3)
        self.assertTrue(all(resultado.valor < 10 for resultado in resultados))

    def test_eliminar_existente(self):
        self.arbol.eliminar(5)
        resultado = self.arbol.buscar(5)
        self.assertIsNone(resultado)

    def test_eliminar_no_existente(self):
        self.arbol.eliminar(20)
        resultado = self.arbol.buscar(20)
        self.assertIsNone(resultado)

    def test_eliminarAll_existente(self):
        self.arbol.eliminarAll(5)
        resultados = self.arbol.buscarAll(5)
        self.assertEqual(len(resultados), 0)

    def test_eliminarAll_no_existente(self):
        self.arbol.eliminarAll(20)
        resultados = self.arbol.buscarAll(20)
        self.assertEqual(len(resultados), 0)

    def test_eliminarWhere_proposicion(self):
        def es_menor_que_10(nodo: Optional[NodoInterface]) -> bool:
            return nodo is not None and nodo.valor < 10

        self.arbol.eliminarWhere(es_menor_que_10)
        resultados = self.arbol.buscarWhere(es_menor_que_10)
        self.assertEqual(len(resultados), 0)


if __name__ == '__main__':
    unittest.main()