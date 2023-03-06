import os
import shutil

os.environ['V8_FROM_SOURCE'] = '1'
os.system('cross build -vv --target aarch64-linux-android --release')

ver = 'v0.60.1'
src = './target/aarch64-linux-android/release/gn_out/obj/librusty_v8.a'
dst_dir = f'../Dist/rusty_v8/{ver}'
dst = f'{dst_dir}/librusty_v8.a'

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

shutil.copy(src, dst)
