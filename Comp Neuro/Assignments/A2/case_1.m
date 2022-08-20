
% Generate the null-cline plots for the FitzHugh Nagumo neuron model
% These are the zero derivative points for v and w

% assign the fixed parameters
a = 0.5;
b = 0.1;
r = 0.1;

% Choose the value of the input current 
I_ext = 0;
dt = 0.01

%% (b)

% Generate the phase plots for different values of initial V
% Below we do it for the case where v0 < a (0.2) and I = 0

[v_phase,w_phase] = fhn(0,0.2,0,a,b,r);
hold on
subplot(1,4,1)
% For v0 = 1 we plot the response versus time curves
time=0:0.05:100;
plot(time,v_phase);
ylabel({'V'});
xlabel({'time (s)'});
title({'V vs time'});

subplot(1,4,2)
plot(time,w_phase);
ylabel({'W'});
xlabel({'time (s)'});
title({'W vs time'});
%% (c)

% Generate the phase plots for different values of initial V
% Below we do it for the case where v0 > a (0.6) and I = 0
    
[v_phase,w_phase] = fhn(0,0.6,0,a,b,r);

subplot(1,4,3)
% For v0 = 1 we plot the response versus time curves
time=0:0.05:100;
plot(time,v_phase);
ylabel({'V'});
xlabel({'time (s)'});
title({'V vs time'});

subplot(1,4,4)
plot(time,w_phase);
ylabel({'W'});
xlabel({'time (s)'});
title({'W vs time'});

