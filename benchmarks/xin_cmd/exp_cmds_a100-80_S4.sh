## a100-80 S4

# exp for the main table
# python launch_server.py  --device a100-80  --model-setting S4  --backend slora  --num-adapter 100  --num-token 65000 --dummy
python ../run_exp.py  --backend slora  --suite a100-80-xin  --model-setting S4  --mode synthetic  --output xin_synthetic_num_adapters_a100-80_S4_slora_table.jsonl --append
