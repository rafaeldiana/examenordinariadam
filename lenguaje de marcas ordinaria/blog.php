<!DOCTYPE html>
<html>
<head>
    <title>Web de José Vicente - Blog</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <header>
        <h1>Web de José Vicente</h1>
    </header>
    <nav>
        <ul>
            <li><a href="index.html">Inicio</a></li>
            <li><a href="about.html">Sobre mi</a></li>
            <li><a href="blog.php">Blog</a></li>
            <li><a href="contact.html">Contacto</a></li>
        </ul>
    </nav>
    <main>
        <h2>Blog</h2>
        <?php
        // Conexión a la base de datos
        $conexion = mysqli_connect("localhost", "usuario", "contraseña", "basedatos");

        // Consulta para obtener las entradas del blog
        $consulta = "SELECT * FROM entradas ORDER BY fecha DESC";
        $resultado = mysqli_query($conexion, $consulta);

        // Mostrar las entradas del blog
        while ($entrada = mysqli_fetch_assoc($resultado)) {
            echo "<h3>" . $entrada['titulo'] . "</h3>";
            echo "<p>" . $entrada['texto'] . "</p>";
            echo "<hr>";
        }

        // Cerrar conexión a la base de datos
        mysqli_close($conexion);
        ?>
    </main>
    <footer>
        <!-- Pie de página -->
    </footer>
</body>
</html>
