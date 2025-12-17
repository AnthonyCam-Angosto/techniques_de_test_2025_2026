"""Module de triangulation utilisant l'algorithme de Bowyer-Watson."""
from src.object import Point, Triangle


class TriangulationError(Exception):
    """Exception s'il y a des erreur durant la triangulation."""

    pass


def start(points:list[Point])->list[Triangle]:
    """Fonction principal de la triangulation.
    
    :param points: liste de point
    :type points: list[Point]
    :return: liste des triangles trouvé
    :rtype: list[Triangle]
    """
    if(points is None):
            raise TriangulationError("erreur pointset inexistant")
    if(len(points)==0):
            raise TriangulationError("erreur pointset vide")
    
    try:
        triangles=bowyer_watson(points)
    except Exception as err:
        raise TriangulationError("erreur durant la triangulation") from err

    return triangles


def det(a: Point, b: Point, c: Point) -> float:
    """Calcule le déterminant de trois points.
    
    :param a: point a
    :type a: Point
    :param b: point b
    :type b: Point
    :param c: point c
    :type c: Point
    :return: valeur du déterminant
    :rtype: float
    """# noqa: D401
    return (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)


def circumcircle_contains(tri: Triangle, p: Point) -> bool:
    """Verification si le point est de dans le rayon du triangle.
    
    :param tri: triangle
    :type tri: Triangle
    :param p: point à verfier
    :type p: Point
    :return: indique si le point est dans le rayon
    :rtype: bool
    """
    ax, ay = tri.point1.x, tri.point1.y
    bx, by = tri.point2.x, tri.point2.y
    cx, cy = tri.point3.x, tri.point3.y
    dx, dy = p.x, p.y

    ax -= dx 
    ay -= dy
    bx -= dx 
    by -= dy
    cx -= dx 
    cy -= dy

    a2 = ax*ax + ay*ay
    b2 = bx*bx + by*by
    c2 = cx*cx + cy*cy

    det_circle = (
        ax * (by * c2 - b2 * cy)
        - ay * (bx * c2 - b2 * cx)
        + a2 * (bx * cy - by * cx)
    )

    orientation = det(tri.point1, tri.point2, tri.point3)
    if orientation < 0:
        det_circle = -det_circle

    return det_circle > 0


def make_supertriangle(points):
    """Creation d'un triangle contenant tout les points.
    
    :param points: liste de points
    """
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    dx = maxx - minx
    dy = maxy - miny
    dmax = max(dx, dy)
    midx = (minx + maxx) / 2.0
    midy = (miny + maxy) / 2.0

    p1 = Point(midx - 2*dmax, midy - dmax)
    p2 = Point(midx,midy + 2*dmax)
    p3 = Point(midx + 2*dmax, midy - dmax)

    return Triangle(p1, p2, p3)


def edge_key(e):
    """Création d'une clé unique pour une arête.

    :param e: arête
    :type e: tuple[Point, Point]
    :return: clé unique
    :rtype: tuple[tuple[float, float], tuple[float, float]].
    """
    a, b = e
    return tuple(sorted([(a.x, a.y), (b.x, b.y)]))


def unique_boundary_edges(edges):
    """Retourne les arêtes uniques parmi une liste d'arêtes.

    :param edges: liste d'arêtes
    :type edges: list[tuple[Point, Point]]
    :return: liste des arêtes uniques
    :rtype: list[tuple[Point, Point]].
    """
    count = {}
    for e in edges:
        k = edge_key(e)
        count[k] = count.get(k, 0) + 1

    unique = []
    for e in edges:
        if count[edge_key(e)] == 1:
            unique.append(e)
    return unique


def bowyer_watson(points):
    """Triangulation de Delaunay par l'algorithme de Bowyer-Watson.

    :param points: liste de point
    :type points: list[Point]

    """
    if len(points) < 3:
        return []
    
    super_tri = make_supertriangle(points)
    triangulation = [super_tri]

    for p in points:
        bad = []
        for tri in triangulation:
            if circumcircle_contains(tri, p):
                bad.append(tri)

        edges = []
        for tri in bad:
            edges.extend(tri.edges())

        triangulation = [t for t in triangulation if t not in bad]

        boundary = unique_boundary_edges(edges)

        for (a, b) in boundary:
            if det(a, b, p) <= 0:
                a, b = b, a
            triangulation.append(Triangle(a, b, p))

    s_points = set(super_tri.get_points())
    final = []
    for tri in triangulation:
        if (
            (tri.point1 in s_points) 
            or (tri.point2 in s_points) 
            or (tri.point3 in s_points)
        ):
            continue
        final.append(tri)

    return final