import mongoose from 'mongoose';

const orderSchema = new mongoose.Schema({
  propertyAddress: String,
  buyer: String,
  seller: String,
  purchasePrice: Number,
  titleOfficer: String,
  fileNumber: { type: String, unique: true },
  documents: [String],
  searchType: String,
  county: String,
  state: String,
  vesting: String,
  parcel: String,
  instructions: String,
  searches: [{
    name: String,
    completed: { type: Boolean, default: false },
    resultFile: String
  }],
  status: { type: String, enum: ['New', 'In Progress', 'Completed'], default: 'New' },
  assignedTo: String,
  owner: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
}, { timestamps: true });

export default mongoose.model('Order', orderSchema);
