import express from 'express';
import multer from 'multer';
import Order from '../models/Order.js';
import { auth, adminOnly } from '../middleware/auth.js';

const router = express.Router();
const upload = multer({ dest: 'uploads/' });

router.post('/', auth, async (req, res) => {
  try {
    const count = await Order.countDocuments();
    const fileNumber = `F-${count + 1}`;
    const order = new Order({ ...req.body, owner: req.user._id, fileNumber });
    await order.save();
    res.json(order);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

router.get('/', auth, async (req, res) => {
  const filter = req.user.role === 'admin' ? {} : { owner: req.user._id };
  const orders = await Order.find(filter);
  res.json(orders);
});

router.get('/:id', auth, async (req, res) => {
  const order = await Order.findById(req.params.id);
  if (!order) return res.status(404).json({ message: 'Not found' });
  if (req.user.role !== 'admin' && !order.owner.equals(req.user._id)) {
    return res.status(403).json({ message: 'Forbidden' });
  }
  res.json(order);
});

router.patch('/:id', auth, adminOnly, async (req, res) => {
  const order = await Order.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(order);
});

router.post('/:id/upload', auth, upload.single('file'), async (req, res) => {
  const order = await Order.findById(req.params.id);
  if (!order) return res.status(404).json({ message: 'Not found' });
  if (req.user.role !== 'admin' && !order.owner.equals(req.user._id)) {
    return res.status(403).json({ message: 'Forbidden' });
  }
  order.documents.push(req.file.path);
  await order.save();
  res.json(order);
});

export default router;
