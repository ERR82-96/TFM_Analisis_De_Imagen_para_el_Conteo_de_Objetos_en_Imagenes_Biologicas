# TFM: Análisis de Imagen para el Conteo de Objetos en Imágenes Biológicas

Estimar el número de objetos o partículas en una imagen o en un video, que al final es una secuencia de imágenes, es algo en lo que siempre ha habido intereses, desde el gobierno para controlar a sus habitantes, hasta organizaciones ecológicas para llevar control de poblaciones de ciertas especies de fauna y flora. El primer método para contar partículas en una imagen que a cualquiera se le ocurre es hacerlo a mano, pero normalmente se espera tener que contar un gran número de partículas, resultando el método manual demasiado cansado. El método CountEm utiliza un muestreo geométrico y sistemático para realizar una estimación del tamaño de la población pseudo-manual, superpone una rejilla de ventanas de muestreo definida por unos parámetros sobre la imagen y se contarán las partículas de dichas ventanas de muestreo para dar una estimación. Esto convierte una tarea tediosa y poco práctica de contar a mano, en algo más simple, más fácil de verificar y que no consume tanto tiempo, esto no quiere decir que no se pueda mejorar.

En este proyecto trataremos de buscar un método que pueda dar una estimación inicial del tamaño de la población para que CountEm pueda elegir unos parámetros iniciales para la rejilla más adecuados y de manera automática. Para ello se estudiarán y analizarán dos métodos de procesado digital de imágenes, uno de ellos más simple y otro estará basado en machine learning.

***
Repositorio del trabajo de fin de máster de Eduardo Ruiz Ruiz para el máster de Ciencia de Datos, donde están disponibles los notebooks con el código de las pruebas realizadas y otros archivos relevantes del proyecto.
