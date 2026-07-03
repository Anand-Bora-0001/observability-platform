import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Server, Activity, AlertTriangle, CheckCircle } from 'lucide-react';

const mockData = [
  { time: '10:00', cpu: 45, memory: 60 },
  { time: '10:05', cpu: 55, memory: 62 },
  { time: '10:10', cpu: 40, memory: 58 },
  { time: '10:15', cpu: 85, memory: 75 },
  { time: '10:20', cpu: 65, memory: 70 },
  { time: '10:25', cpu: 50, memory: 65 },
];

const MetricCard = ({ title, value, icon, trend }: { title: string, value: string, icon: React.ReactNode, trend: string }) => (
  <div className="bg-gray-900 border border-gray-800 rounded-xl p-6 shadow-sm">
    <div className="flex justify-between items-start">
      <div>
        <p className="text-gray-400 text-sm font-medium">{title}</p>
        <h3 className="text-white text-3xl font-bold mt-2">{value}</h3>
      </div>
      <div className="p-3 bg-gray-800 rounded-lg text-blue-400">
        {icon}
      </div>
    </div>
    <div className="mt-4 text-sm text-gray-400">
      <span className={trend.startsWith('+') ? 'text-green-400' : 'text-red-400'}>{trend}</span> since last hour
    </div>
  </div>
);

const Dashboard: React.FC = () => {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-white">Infrastructure Overview</h1>
        <p className="text-gray-400">Real-time metrics and system health</p>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <MetricCard title="Total Servers" value="124" icon={<Server size={24} />} trend="+3" />
        <MetricCard title="Avg CPU Usage" value="45%" icon={<Activity size={24} />} trend="-2%" />
        <MetricCard title="Active Incidents" value="2" icon={<AlertTriangle size={24} className="text-yellow-500" />} trend="+1" />
        <MetricCard title="System Uptime" value="99.9%" icon={<CheckCircle size={24} className="text-green-500" />} trend="Stable" />
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
          <h3 className="text-white font-medium mb-4">CPU Usage (Average)</h3>
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="time" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1F2937', border: 'none', borderRadius: '8px', color: '#fff' }} 
                  itemStyle={{ color: '#60A5FA' }}
                />
                <Line type="monotone" dataKey="cpu" stroke="#3B82F6" strokeWidth={3} dot={{ r: 4 }} activeDot={{ r: 6 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="bg-gray-900 border border-gray-800 rounded-xl p-6">
          <h3 className="text-white font-medium mb-4">Memory Usage (Average)</h3>
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="time" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1F2937', border: 'none', borderRadius: '8px', color: '#fff' }} 
                  itemStyle={{ color: '#A78BFA' }}
                />
                <Line type="monotone" dataKey="memory" stroke="#8B5CF6" strokeWidth={3} dot={{ r: 4 }} activeDot={{ r: 6 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
