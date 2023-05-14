import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(
  "stockfish_15.1_win_x64_popcnt/stockfish-windows-2022-x86-64-modern.exe"
)

board = chess.Board()

result = engine.play(board, chess.engine.Limit(time=2.0))
best_move = result.move

board.push(best_move)

engine.quit()
