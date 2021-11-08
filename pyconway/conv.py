import numpy as np


def conv2dconway(arr,  boundary='fill'):
    assert(boundary in ['fill', 'wrap'])
    assert(arr.ndim == 2)

    ah, aw = arr.shape[:2]

    _arr = arr.astype(np.uint8)
    if boundary == 'wrap':
        _arr = np.hstack((_arr[:,-1].reshape(ah, 1),   _arr, _arr[:,0].reshape(ah, 1)))
        _arr = np.vstack((_arr[-1,:].reshape(1, aw+2), _arr, _arr[0,:].reshape(1, aw+2)))
    else:
        _arr = np.zeros((ah+2, aw+2), dtype=np.uint8)
        _arr[1:-1, 1:-1] = arr 

    new_arr = np.zeros(_arr.shape, dtype=np.uint8)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            new_arr[1:-1, 1:-1] += _arr[i:i+ah, j:j+aw]

    out = new_arr[1:-1, 1:-1]
    return out


def conv3dconway(arr3d, boundary='fill'):
    assert(boundary in ['fill', 'wrap'])
    assert(arr3d.ndim == 3)

    ah, aw, ad = arr3d.shape[:3]

    _arr3d = arr3d.astype(np.uint8)
    if boundary == 'wrap':
        _arr3d = np.dstack((_arr3d[:,:,-1].reshape(ah, aw, 1), _arr3d, _arr3d[:,:,0].reshape(ah, aw, 1)))
        _arr3d = np.hstack((_arr3d[:,-1,:].reshape(ah, 1, ad+2), _arr3d, _arr3d[:,0,:].reshape(ah, 1, ad+2)))
        _arr3d = np.vstack((_arr3d[-1,:,:].reshape((1, aw+2, ad+2)),_arr3d, _arr3d[0,:,:].reshape((1, aw+2, ad+2))))
    else:
        _arr3d = np.zeros((ah+2, aw+2, ad+2), dtype=np.uint8)
        _arr3d[1:-1, 1:-1, 1:-1] = arr3d

    new_arr = np.zeros(_arr3d.shape, dtype=np.uint8)

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if i == 1 and j == 1 and k == 1:
                    continue
                new_arr[1:-1, 1:-1, 1:-1] += _arr3d[i:i+ah, j:j+aw, k:k+ad]

    out = new_arr[1:-1, 1:-1, 1:-1]
    return out
