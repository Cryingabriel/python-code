import pygame
import random
from pygame.math import Vector2


FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")


# definitions:
def add_vertex(v: int):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []



# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1: int, v2: int, e: int):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)
# driver code
graph: dict[int, list[list[int]]] = {}
# stores the number of vertices in the graph
vertices_no = 0
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.

print(graph)

def main():
  # game setup:
  #clock = pygame.time.Clock()

  positions: list[Vector2] = []
  for i in graph:
    positions.append(Vector2(random.randrange(1200), random.randrange(800)))

  # main loop:
  running = True
  while running:
    #delta = clock.tick(FRAMERATE) / 1000

    # input:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # draw:
    screen.fill("#000000")
    for i in range(len(graph)):
      pygame.draw.circle(screen, (255, 125, 0), positions[i], 10)


    for t in graph:
      for g in graph[t]:
        pygame.draw.line(screen, (255, 125, 0), positions[t-1], positions[g[0]-1])
    pygame.display.flip()

if __name__ == "__main__":
  main()