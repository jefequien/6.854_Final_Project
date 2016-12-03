class ImageSegmenter:

    def __init__(self, pixels):
        height, width, colors = pixels.shape

        self.graph = ImageGraph(pixels)

        self.solver = Ford_Fulkerson()
        self.solver = Blocking_Flows()

        self.segmented_image = np.zeros((height, width))

    def segment(self):
        for i in xrange(100):
            s = self.graph.randomNode()
            t = self.graph.randomNode()
            min_cut = self.solver.find_min_cut(graph, s, t)

        for edge in min_cut:
            u = edge.u
            v = edge.v
            self.segmented_image[u.x][u.y] = 1.0
            self.segmented_image[v.x][v.y] = 1.0



