from audioop import add
import pygame
import random
from pygame.math import Vector2
import math
SCREEN_SIZE = Vector2(1200,800)
FRAMERATE = 60
# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")
font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
r = []
for i in range(5):
  q = random.randint(0,5)
  r.append(q)

y = 0
class point():

  # definitions:
  def vertex(self, v: int, position, graph):
    global vertices_no
    if v in graph:
      print("Vertex ", v, " already exists.")
    else:
      vertices_no = vertices_no + 1
      graph[v] = []
      for i in graph:
        position.append(Vector2(random.randrange(1200), random.randrange(800)))
    for i in range(len(graph)):
      pygame.draw.circle(screen, (255, 0, 0), position[i], 10)

class line():
# Add an edge between vertex v1 and v2 with edge weight e
  def edges(self, v1: int, v2: int, e, position, graph):
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
    for t in graph:
      for p in graph[t]:
        start = position[t-1]
        end = position[p[0]-1]
        line_length = start.distance_to(end)
        scaled_length = int(line_length / SCREEN_SIZE.length() * 255)
        # Color Coding to weight
        red = scaled_length
        blue = int(scaled_length / 199)
        green = 255 -scaled_length
        #Text of the edge weight
        text = font.render(str(int(line_length)), True, (red, green, blue))
        midpoint = (start + end)/2

        #drawing the text & edges to screen
        screen.blit(text, midpoint)
        pygame.draw.line(screen, (red, green, blue), start, end)
# driver code
graph: dict[int, list[list[int]]] = {}
# stores the number of vertices in the graph
vertices_no = 0

points = point()
q = []
edge = line()
w = []

# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.

print(graph)

def main():
  # game setup:
  #clock = pygame.time.Clock()

  position: list[Vector2] = []

  # main loop:
  running = True
  while running:
    #delta = clock.tick(FRAMERATE) / 1000

    # input:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # draw:
    screen.fill((0,0,0))

    q.append(points.vertex(1, position, graph))
    q.append(points.vertex(2, position, graph))
    q.append(points.vertex(3, position, graph))
    w.append(edge.edges(1, 2, 0, position, graph))
    w.append(edge.edges(1, 3, 1, position, graph))
    print(r)
    pygame.display.flip()

if __name__ == "__main__":
  main()