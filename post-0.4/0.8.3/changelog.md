Bugfix regarding Quaternion.eulerAngles.

To set the rotation of the camera using Euler angles,
use `scene.mainCamera.localRotation.SetBackward(Vector3(...))`.