perl -pi -e 's|execution_count": null|execution_count": 1|g' course-v4/nbs/*ipynb
nohup jupyter notebook --no-browser --allow-root --ip=0.0.0.0&