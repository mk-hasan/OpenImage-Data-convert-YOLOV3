import tensorflow as tf

meta_path = '/home/jupyter/repo/tensorflow-yolo-v3/saved_model/model.ckpt.meta' # Your .meta file
output_node_names = ['output:0']    # Output nodes

with tf.Session() as sess:
    
    # Restore the graph
    saver = tf.train.import_meta_graph(meta_path)

    # Load weights
    saver.restore(sess,tf.train.latest_checkpoint('/home/jupyter/repo/tensorflow-yolo-v3/saved_model/'))

    # Freeze the graph
    frozen_graph_def = tf.graph_util.convert_variables_to_constants(
        sess,
        sess.graph_def,
        output_node_names)

    # Save the frozen graph
    with open('/home/jupyter/repo/tensorflow-yolo-v3/output_graph.pb', 'wb') as f:
        f.write(frozen_graph_def.SerializeToString())