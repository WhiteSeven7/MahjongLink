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
        self.rect = self.image.get_rect(topleft=(pos[0] * 50 + 3, pos[1] * 50 + 3))
        # 根据id着色
        self.image.fill(self.colors[self.id])
        # map
        self._map = None

    
    def set_map(self, map: dict[tuple[int, int], "Mahjong"]):
        self._map = map

    def kill(self) -> None:
        del self._map[self.pos]
        return super().kill()


class MahjongGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.map: dict[tuple[int, int], Mahjong] = {}

    def add(self, *sprites: Mahjong) -> None:
        for mahjong in sprites:
            mahjong.set_map(self.map)
            self.map[mahjong.pos] = mahjong
        return super().add(*sprites)


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("连连看")
        self.surface = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.quit = False
        # 所有麻将
        self.mahjong_group = MahjongGroup()
        # 麻将桌的尺寸
        self.mohjong_x, self.mahjong_y = 12, 10
        # 生成麻将
        self.add_mohjong()
        # 被点击的麻将
        self.clicked_mohjong: list[Mahjong] = []


    def control(self):
        event: pygame.event.Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
                continue
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mohjong: Mahjong
                for mohjong in self.mahjong_group:
                    if mohjong.rect.collidepoint(event.pos):
                        self.clicked_mohjong.append(mohjong)
                        break


    def update(self):
        if len(self.clicked_mohjong) < 2:
            return
        a, b, *_ = self.clicked_mohjong
        if a.id != b.id:
            self.clicked_mohjong.clear()
            return
        print("a == b !!!")
        a.kill()
        b.kill()
        self.clicked_mohjong.clear()
    

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
        for y in range(1, self.mahjong_y - 1):
            for x in range(1, self.mohjong_x - 1):
                self.mahjong_group.add(Mahjong(random.randint(0, 9), (x, y)))

    
    def get_mohjong_path(self, a, b):
        """拿到两个麻将之间的路径或 None"""

        return None



if __name__ == '__main__':
    game = Game()
    game.run()
