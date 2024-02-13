class Solution:
    def floodFillHelper(self, image, sr, sc, color, fillColor):
        if sr < 0 or sr >= len(image):
            return image
        if sc < 0 or sc >= len(image[0]):
            return image
        if image[sr][sc] == color:
            return image
        if not image[sr][sc] == fillColor:
            return image
        image[sr][sc] = color
        self.floodFillHelper(image, sr + 1, sc, color, fillColor)
        self.floodFillHelper(image, sr - 1, sc, color, fillColor)
        self.floodFillHelper(image, sr, sc + 1, color, fillColor)
        self.floodFillHelper(image, sr, sc - 1, color, fillColor)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.floodFillHelper(image, sr, sc, color, image[sr][sc])