import React from 'react';
import { FileText, Download, TrendingUp, AlertTriangle } from 'lucide-react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Week 1', uptime: 99.99, mttr: 4.2 },
  { name: 'Week 2', uptime: 99.98, mttr: 5.1 },
  { name: 'Week 3', uptime: 100.00, mttr: 0 },
  { name: 'Week 4', uptime: 99.95, mttr: 12.5 },
];

const Reports: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-white">SLA & Reports</h1>
          <p className="text-gray-400">Monthly uptime and incident statistics</p>
        </div>
        <button className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white font-medium rounded-lg shadow-sm transition-colors flex items-center space-x-2">
          <Download size={18} />
          <span>Export PDF</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm flex items-center space-x-2"><TrendingUp size={16}/><span>Monthly Uptime</span></p>
          <p className="text-2xl font-bold text-green-400 mt-1">99.98%</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm flex items-center space-x-2"><AlertTriangle size={16}/><span>MTTR (Mean Time to Recovery)</span></p>
          <p className="text-2xl font-bold text-yellow-400 mt-1">5.4 hrs</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm">MTBF (Mean Time Between Failures)</p>
          <p className="text-2xl font-bold text-blue-400 mt-1">168 hrs</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Total Incidents</p>
          <p className="text-2xl font-bold text-white mt-1">12</p>
        </div>
      </div>

      <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
        <h2 className="text-lg font-semibold text-white mb-4">Uptime Trend (30 Days)</h2>
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" vertical={false} />
              <XAxis dataKey="name" stroke="#9CA3AF" />
              <YAxis stroke="#9CA3AF" domain={[99.00, 100.00]} />
              <Tooltip
                contentStyle={{ backgroundColor: '#1F2937', border: 'none', borderRadius: '0.5rem', color: '#fff' }}
              />
              <Line type="monotone" dataKey="uptime" stroke="#10B981" strokeWidth={3} dot={{ r: 4 }} activeDot={{ r: 6 }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default Reports;
