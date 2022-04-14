import os
import pygame
from game import Game
import neat 
import pickle

WIDTH = 600
HEIGHT = 700
SPEED = 20
fps = 30

def play_game():
    game = Game(WIDTH, HEIGHT)

    clock = pygame.time.Clock()
    run = True
    keypress = False
    
    while(run):
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys=pygame.key.get_pressed()
        jumping = False
        if keys[pygame.K_SPACE]:
            jumping=True
        
        game.bird.jump(jumping)
        
        if game.update() is not None:
            return 

        pygame.display.update()
    pygame.display.quit()
    pygame.quit()

def train_ai(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        game = Game(WIDTH, HEIGHT)

        clock = pygame.time.Clock()
        run = True
        keypress = False
        
        while(run):
            # clock.tick(fps)

            (bird_y, closest_pipe_bottom, closest_pipe_top) = game.getGameInfo()
            output = net.activate((bird_y, closest_pipe_bottom, closest_pipe_top))
            decision = output.index(max(output))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            game.bird.jump(decision)
            
            if game.update() is not None:
                genome.fitness = game.score 
                run=False

            pygame.display.update()
    pygame.display.quit()
    pygame.quit()


def test_ai(net):
    game = Game(WIDTH, HEIGHT)

    clock = pygame.time.Clock()
    run = True
    keypress = False
    
    while(run):
        clock.tick(fps)

        (bird_y, closest_pipe_bottom, closest_pipe_top) = game.getGameInfo()
        output = net.activate((bird_y, closest_pipe_bottom, closest_pipe_top))
        decision = output.index(max(output))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        game.bird.jump(decision)
        
        if game.update() is not None:
            run=False

        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


def test_best_network():
    with open("best.pickle", "rb") as f:
        winner = pickle.load(f)
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                            neat.DefaultSpeciesSet, neat.DefaultStagnation,
                            config_path)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    test_ai(winner_net)


def run_neat():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-1')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(train_ai, 50)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    print("Press 1 to play yourself (spacebar to jump)")
    print("Press 2 to train AI")
    print("Press 3 to run AI (after training)")
    inp = input("")
    if inp=='1':
        play_game()
    if inp=='2':
        run_neat()
    if inp=='3':
        test_best_network()
