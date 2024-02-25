import pygame
import sys
import random


SIZE = WIDTH, HEIGHT = 600, 600


class Mahjong(pygame.sprite.Sprite):
    colors = [
        "#ED1C24",  # 红
        "#FF7F27",  # 橙
        "#FFF200",  # 黄
        "#22B14C",  # 绿
        "#00A2E8",  # 青
        "#3F48CC",  # 蓝
        "#A349A4",  # 紫
        "#FFAEC9",  # 粉
        "#B5E61D",  # 酸绿
        "#7F82BB",  # 淡紫色
    ]
    def __init__(self, id: int, pos: tuple[int, int]) -> None:
        super().__init__()
        # id一致可以消除
        self.id = id
        # 位置
        self.pos = pos 
        # 图像
        self.image = pygame.surface.Surface((44, 44))
        # 矩形
        self.rect = self.image.get_rect(topleft=(pos[0] * 50, pos[1] * 50))
        # 根据id着色
        self.image.fill(self.colors[self.id])


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("连连看")
        self.surface = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.quit = False
        # 所有麻将
        self.mahjong_group = pygame.sprite.Group()
        # 生成麻将
        self.add_mohjong()


    def control(self):
        event: pygame.event.Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mahjong_group.empty()
                self.add_mohjong()


    def update(self):
        ...
    

    def draw(self):
        self.surface.fill("#C3C3C3")
        self.mahjong_group.draw(self.surface)
        pygame.display.flip()


    def run(self):
        while not self.quit:
            self.control()
            self.update()
            self.draw()
            self.clock.tick(60)
        self.safe_quit()


    def safe_quit(self):
        pygame.quit()
        sys.exit()


    def add_mohjong(self) -> None:
        """生成麻将"""
        for y in range(8):
            for x in range(10):
                self.mahjong_group.add(Mahjong(random.randint(0, 9), (x, y)))



if __name__ == '__main__':
    game = Game()
    game.run()
