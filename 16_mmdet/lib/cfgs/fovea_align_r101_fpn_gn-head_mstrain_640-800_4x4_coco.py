# model settings
model = dict(
    type='FOVEA',
    pretrained='torchvision://resnet101',
    backbone=dict(
        type='ResNet',
        depth=101,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch'),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        start_level=1,
        num_outs=5,
        add_extra_convs='on_input'),
    bbox_head=dict(
        type='FoveaHead',
        num_classes=80,
        in_channels=256,
        stacked_convs=4,
        feat_channels=256,
        strides=[8, 16, 32, 64, 128],
        base_edge_list=[16, 32, 64, 128, 256],
        scale_ranges=((1, 64), (32, 128), (64, 256), (128, 512), (256, 2048)),
        sigma=0.4,
        with_deform=True,
        norm_cfg=dict(type='GN', num_groups=32, requires_grad=True),
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=1.50,
            alpha=0.4,
            loss_weight=1.0),
        loss_bbox=dict(type='SmoothL1Loss', beta=0.11, loss_weight=1.0)))
# training and testing settings
train_cfg = dict()
test_cfg = dict(
    nms_pre=1000,
    score_thr=0.05,
    nms=dict(type='nms', iou_threshold=0.5),
    max_per_img=100)






#Dataset Settings
dataset_type = 'CocoDataset'
data_root = ''
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='Resize',
        img_scale=[(1333, 640), (1333, 800)],
        multiscale_mode='value',
        keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=,    #change1
    workers_per_gpu=,    #change2
    train=dict(
        type=dataset_type,
        classes=,          #change3
        ann_file=,         #change4
        img_prefix=,       #change5
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        classes=,          #change6
        ann_file=,         #change7
        img_prefix=,       #change8
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        classes=,          #change9
        ann_file=,         #change10
        img_prefix=,       #change11
        pipeline=test_pipeline))
evaluation = dict(interval=, metric='bbox')     #change9




# Schedule Settings
optimizer = dict(type='SGD', lr=, momentum=, weight_decay=)     #change12
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=)           #change13
total_epochs =       #change14




# Runtime Dataset
checkpoint_config = dict(interval=)    #change15
# yapf:disable
log_config = dict(
    interval=50,           #change16
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from =                   #change17
resume_from = None
workflow = [('train', 1)]

gpu_ids = None                #change18


